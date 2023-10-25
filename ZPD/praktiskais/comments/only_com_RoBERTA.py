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
import re

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

        while request is not None:
            response = request.execute()

            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                self.comments.append({
                    'author': comment['authorDisplayName'],
                    'published_at': comment['publishedAt'],
                    'updated_at': comment['updatedAt'],
                    'like_count': comment['likeCount'],
                    'text': comment['textDisplay'],
                })

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

    def save_comments_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.comments, f, ensure_ascii=False, indent=4)
    
    def count_comments(self):
        total_comments = len(self.comments)
        print(f"Total Comments: {total_comments}")


class Combine:
    def mix_Rep_and_com(self):
        with open('praktiskais/comments/jsons/comments.json', 'r', encoding='utf-8') as f:
            comments_data = json.load(f)

        def remove_links(text):
            return re.sub(r'http\S+', '', text)

        def remove_mentions(text):
            return re.sub(r'@\w+', '', text)
        
        def remove_mentions(text):
            return re.sub(r'<herf+', '', text)
        
        def remove_mentions(text):
            return re.sub(r'[^\w]', ' ', text)
        
        def remove_mentions(text):
            return re.sub(r'[^a-z\s]+', ' ', text)
        
        def remove_mentions(text):
            return re.sub(r'(\s+)', ' ', text)
        
        def remove_mentions(text):
            return re.sub(r'\[[^]]*\]', ' ', text)
    
        output_data = []
        for comment in comments_data:
            cleaned_text = remove_mentions(remove_links(comment["text"]))
            output_data.append({"text": clean(cleaned_text, no_emoji=True)})
            for reply in comment.get("replies", []):
                cleaned_reply = remove_mentions(remove_links(reply))
                output_data.append({"text": clean(cleaned_reply, no_emoji=True)})

        with open('praktiskais/comments/jsons/mix_C&R.json', 'w', encoding='utf-8') as file:
            json.dump(output_data, file, indent=4, ensure_ascii=False)

class Detect_Language:

    def detect_lang(self):

        with open('praktiskais/comments/jsons/mix_C&R.json', 'r', encoding='utf-8') as f:
            comments = json.load(f)
        
        comments_not_in_english = []
        comments_in_english = []

        for comment in comments:
            text = comment.get("text")
            if text and len(text) > 3:
                try:
                    language = detect(text)
                    if language != "en":
                        comments_not_in_english.append({"text": text, "language": language})
                    else:
                        comments_in_english.append({"text": text})
                except Exception as _:
                    print(f"An error occurred, empty 'text' list in comments.json")

        if comments_in_english:
            with open('praktiskais/comments/jsons/only_english.json', 'w', encoding='utf-8') as f:
                json.dump(comments_in_english, f, ensure_ascii=False, indent=4)

        if comments_not_in_english:
            with open('praktiskais/comments/jsons/comments_not_in_eng.json', 'w', encoding='utf-8') as f:
                json.dump(comments_not_in_english, f, ensure_ascii=False, indent=4)

class Translate_All_Comments:

    def translate(self):
        translator = Translator()

        with open('praktiskais/comments/jsons/comments_not_in_eng.json', 'r', encoding='utf-8') as f:
            comments_data = json.load(f)

        translated_comments = []
        for comment in comments_data:
            translated_text = translator.translate(comment['text'], src=comment['language'], dest='en')
            translated_comments.append({'text': translated_text.text})

        with open('praktiskais/comments/jsons/only_english.json', 'r', encoding='utf-8') as f:
            english_comments = json.load(f)

        translated_comments.extend(english_comments)

        with open('praktiskais/comments/jsons/translated.json', 'w', encoding='utf-8') as f:
            json.dump(translated_comments, f, indent=4)

class SentimentAnalyzer:

    MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
    LABEL_MAPPING_LINK = "https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/sentiment/mapping.txt"
    INPUT_FILE = 'praktiskais/comments/jsons/translated.json'
    OUTPUT_FILE = 'praktiskais/comments/jsons/sentiment.json'

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL)
        self.labels = self._download_label_mapping()
        self.model = AutoModelForSequenceClassification.from_pretrained(self.MODEL)

    def _download_label_mapping(self):
        labels = []
        with urllib.request.urlopen(self.LABEL_MAPPING_LINK) as f:
            html = f.read().decode('utf-8').split("\n")
            csvreader = csv.reader(html, delimiter='\t')
            labels = [row[1] for row in csvreader if len(row) > 1]
        return labels

    def analyze_sentiment(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
        output = self.model(**inputs)
        scores = output.logits[0].detach().numpy()
        scores = softmax(scores)

        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        result_item = {"text": text}

        for i in range(scores.shape[0]):
            label = self.labels[ranking[i]]
            score = np.round(float(scores[ranking[i]]), 4)
            result_item[label] = score

        return result_item

    def analyze_sentiments_in_json(self):
        with open(self.INPUT_FILE, 'r') as json_file:
            data = json.load(json_file)

        sentiment_results = []
        for item in data:
            text = item.get('text', '')
            if text:
                result_item = self.analyze_sentiment(text)
                sentiment_results.append(result_item)

        with open(self.OUTPUT_FILE, 'w') as json_output_file:
            json.dump(sentiment_results, json_output_file, indent=4, separators=(',', ': '))


# developer_key = "AIzaSyBrlZLMhq1thWEuGp6bxQufQka7fUUj9b4"
# video_id = "FcN3HnQz3y4"
# print("loading...")
# scrape = Scrape_Comments(developer_key)
# scrape.get_comments(video_id)
# scrape.save_comments_to_json('praktiskais/comments/jsons/comments.json')
# scrape.count_comments()

# combine = Combine()
# combine.mix_Rep_and_com()

# detect_lang = Detect_Language()
# detect_lang.detect_lang()

# print("started translating...")
# translate_all = Translate_All_Comments()
# translate_all.translate()
# print("done!")

print("started sentiment...")
sentiment_analyzer = SentimentAnalyzer()
sentiment_analyzer.analyze_sentiments_in_json()
print("done!")