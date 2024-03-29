from transformers import AutoModelForSequenceClassification, AutoTokenizer
from googletrans import Translator
from scipy.special import softmax
import googleapiclient.discovery
from langdetect import detect
from cleantext import clean
import urllib.request
import numpy as np
import json
import csv
import sys
import re

from transformers import AutoModelForSequenceClassification, AutoTokenizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np

class Scrape_Comments:
    def __init__(self, developer_key):
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.DEVELOPER_KEY = developer_key
        self.youtube = googleapiclient.discovery.build(self.api_service_name, self.api_version, developerKey=self.DEVELOPER_KEY)
        self.comments = []

    def get_comments(self, video_id, max_results=100):
        request = self.youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_results,
            textFormat='plainText'
        )
        comment_id = 1
        while request is not None:
            response = request.execute()
            for item in response['items']:
                
                comment = item['snippet']['topLevelComment']['snippet']
                self.comments.append({
                    'author': comment['authorDisplayName'],
                    'published_at': comment['publishedAt'],
                    'updated_at': comment['updatedAt'],
                    'like_count': comment['likeCount'],
                    'original_text': comment['textDisplay'],
                    'id': comment_id
                })
                comment_id += 1

            if 'nextPageToken' in response:
                request = self.youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    maxResults=max_results,
                    pageToken=response['nextPageToken'],
                    textFormat='plainText'
                )
            else:
                request = None

    def save_comments_to_json(self):
        with open('praktiskais/comments/jsons/comments.json', 'w', encoding='utf-8') as f:
            json.dump(self.comments, f, ensure_ascii=False, indent=4)
    
    def count_comments(self):
        total_comments = len(self.comments)
        sys.stdout.buffer.write(f"Komentāri analizēti: {total_comments}\n".encode('utf-8', 'replace'))

class Detect_Language:

    def detect_lang(self):

        with open('praktiskais/comments/jsons/cleaned.json', 'r', encoding='utf-8') as f:
            comments = json.load(f)
        
        comments_not_in_english = []
        comments_in_english = []

        for comment in comments:
            text = comment.get("text")
            if text and len(text) > 3:
                try:
                    language = detect(text)
                    if language != "en":
                        comments_not_in_english.append({"text": text, "language": language, "id": comment["id"]})
                    else:
                        comments_in_english.append({"text": text, "id": comment["id"]})
                except Exception as _:
                    pass

        if comments_in_english:
            with open('praktiskais/comments/jsons/only_english.json', 'w', encoding='utf-8') as f:
                json.dump(comments_in_english, f, ensure_ascii=False, indent=4)

        if comments_not_in_english:
            with open('praktiskais/comments/jsons/comments_not_in_eng.json', 'w', encoding='utf-8') as f:
                json.dump(comments_not_in_english, f, ensure_ascii=False, indent=4)
                
class Cleaing:
    def clean_text(self):
        with open('praktiskais/comments/jsons/comments.json', 'r', encoding='utf-8') as f:
            comments_data = json.load(f)

        def remove_links(text):
            return re.sub(r'http\S+', '', text)

        def remove_mentions(text):
            return re.sub(r'@\w+', '', text)
        
        def remove_mentions(text):
            return re.sub(r'<href+', '', text)
        
        def remove_mentions(text):
            return re.sub(r'[^\w]', ' ', text)
        
        def remove_mentions(text):
            re.sub(r'[^a-zA-Z\s]', ' ', text)
        
        def remove_mentions(text):
            return re.sub(r'(\s+)', ' ', text)
        
        def remove_mentions(text):
            return re.sub(r'\[[^]]*\]', ' ', text)
    
        output_data = []
        for comment in comments_data:
            cleaned_text = remove_mentions(remove_links(comment["original_text"]))
            cleaned_text = clean(cleaned_text, no_emoji=True)
            output_data.append({"text": cleaned_text, "id": comment["id"]})

        with open('praktiskais/comments/jsons/cleaned.json', 'w', encoding='utf-8') as file:
            json.dump(output_data, file, indent=4, ensure_ascii=False)
class Translate_All_Comments:

    def translate(self):
        translator = Translator()

        with open('praktiskais/comments/jsons/comments_not_in_eng.json', 'r', encoding='utf-8') as f:
            comments_data = json.load(f)

        translated_comments = []
        for comment in comments_data:
            translated_text = translator.translate(comment['text'], src=comment['language'], dest='en')
            translated_comments.append({'text': translated_text.text, "id": comment["id"]})

        with open('praktiskais/comments/jsons/only_english.json', 'r', encoding='utf-8') as f:
            english_comments = json.load(f)

        translated_comments.extend(english_comments)

        with open('praktiskais/comments/jsons/translated.json', 'w', encoding='utf-8') as f:
            json.dump(translated_comments, f, indent=4)

class SentimentAnalyzer:

    ROBERTA_MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
    LABEL_MAPPING_LINK = "https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/sentiment/mapping.txt"
    INPUT_FILE = 'praktiskais/comments/jsons/translated.json'
    OUTPUT_FILE = 'praktiskais/comments/jsons/sentiment.json'

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.ROBERTA_MODEL)
        self.labels = self._download_label_mapping()
        self.model = AutoModelForSequenceClassification.from_pretrained(self.ROBERTA_MODEL)
        self.analyzer = SentimentIntensityAnalyzer()

    def _download_label_mapping(self):
        labels = []
        with urllib.request.urlopen(self.LABEL_MAPPING_LINK) as f:
            html = f.read().decode('utf-8').split("\n")
            csvreader = csv.reader(html, delimiter='\t')
            labels = [row[1] for row in csvreader if len(row) > 1]
        return labels

    def analyze_sentiment_hybrid(self, text, comment_id, like_count, author):
        # Analyze sentiment using RoBERTa
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
        output = self.model(**inputs)
        scores_roberta = output.logits[0].detach().numpy()
        scores_roberta = softmax(scores_roberta)
        ranking_roberta = np.argsort(scores_roberta)
        ranking_roberta = ranking_roberta[::-1]
        result_item_roberta = {"text": text}

        for i in range(scores_roberta.shape[0]):
            label = self.labels[ranking_roberta[i]]
            score = np.round(float(scores_roberta[ranking_roberta[i]]), 4)
            result_item_roberta[label] = score

        # Analyze sentiment using VADER
        sentiment_scores = self.analyzer.polarity_scores(text)
        
        # Combine the scores (You can choose your own logic here)
        combined_score = (result_item_roberta['positive'] + sentiment_scores['compound']) / 2

        # Determine the sentiment label based on the combined score
        if combined_score >= 0.05:
            sentiment_label = 'positive'
        elif combined_score <= -0.05:
            sentiment_label = 'negative'
        else:
            sentiment_label = 'neutral'

        result_item_hybrid = {
            "text": text,
            "combined_score": combined_score,
            "sentiment_label": sentiment_label,
            "id": comment_id,
            "like_count": like_count,
            "author": author
        }

        return result_item_hybrid

    def analyze_sentiments_in_json_hybrid(self):
        with open(self.INPUT_FILE, 'r') as json_file:
            data = json.load(json_file)

        sentiment_results = []
        for item in data:
            text = item.get('text', '')
            comment_id = item.get('id', '')
            like_count = item.get('like_count', 0)
            author_orgin = item.get('author', '')

            if text:
                result_item = self.analyze_sentiment_hybrid(text, comment_id, like_count, author_orgin)
                sentiment_results.append(result_item)

        with open(self.OUTPUT_FILE, 'w') as json_output_file:
            json.dump(sentiment_results, json_output_file, indent=4, separators=(',', ': '))

        return sentiment_results
    
    def sort_comments_by_sentiment(self, results):
        original_comments = {}

        with open('praktiskais/comments/jsons/comments.json', 'r', encoding='utf-8') as comments_file:
            original_comments_data = json.load(comments_file)
            for comment in original_comments_data:
                comment_id = comment.get('id')
                if comment_id is not None:
                    original_comments[comment_id] = {
                        'original_text': comment.get('original_text', ''),
                        'like_count': comment.get('like_count', 0),
                        'author': comment.get('author', '')
                    }

        positive_comments = []
        neutral_comments = []
        negative_comments = []

        for result in results:
            sentiment_label = result['sentiment_label']
            comment_id = result.get('id', '')
            if comment_id in original_comments:
                original_text = original_comments[comment_id]['original_text']
                like_count = original_comments[comment_id]['like_count']
                author_orgin = original_comments[comment_id]['author']
            else:
                original_text = ''
                like_count = 0
                author_orgin = ''

            if sentiment_label == 'positive':
                positive_comments.append({"text": original_text, "id": comment_id, "like_count": like_count, "author": author_orgin})
            elif sentiment_label == 'neutral':
                neutral_comments.append({"text": original_text, "id": comment_id, "like_count": like_count, "author": author_orgin})
            elif sentiment_label == 'negative':
                negative_comments.append({"text": original_text, "id": comment_id, "like_count": like_count, "author": author_orgin})

        paths = {
            'positive': 'praktiskais/sentiment/positive.json',
            'neutral': 'praktiskais/sentiment/neutral.json',
            'negative': 'praktiskais/sentiment/negative.json'
        }

        for label, comments in zip(paths.keys(), [positive_comments, neutral_comments, negative_comments]):
            with open(paths[label], 'w', encoding='utf-8') as f:
                json.dump(comments, f, indent=4, separators=(',', ': '), ensure_ascii=False)


    def calculate_average_scores(self, results):
        total_positive = total_negative = total_neutral = 0
        for result in results:
            sentiment_label = result['sentiment_label']
            if sentiment_label == 'positive':
                total_positive += 1
            elif sentiment_label == 'negative':
                total_negative += 1
            elif sentiment_label == 'neutral':
                total_neutral += 1

        total_entries = len(results)

        average_positive = (total_positive / total_entries) * 100
        average_negative = (total_negative / total_entries) * 100
        average_neutral = (total_neutral / total_entries) * 100

        print(f"Positive: {average_positive:.2f}%")
        print(f"Neutral: {average_neutral:.2f}%")
        print(f"Negative: {average_negative:.2f}%")


with open('praktiskais\server\youtube_id.json', 'r') as json_file:
    data = json.load(json_file)
    youtube_id = data.get('youtube_id', '')

developer_key = "AIzaSyBrlZLMhq1thWEuGp6bxQufQka7fUUj9b4"
video_id = youtube_id
scrape = Scrape_Comments(developer_key)
scrape.get_comments(video_id)
scrape.save_comments_to_json()
scrape.count_comments()

Cleaing = Cleaing()
Cleaing.clean_text()

detect_lang = Detect_Language()
detect_lang.detect_lang()

translate_all = Translate_All_Comments()
translate_all.translate()

sentiment_analyzer = SentimentAnalyzer()
results = sentiment_analyzer.analyze_sentiments_in_json_hybrid()
sentiment_analyzer.sort_comments_by_sentiment(results)
sentiment_analyzer.calculate_average_scores(results)