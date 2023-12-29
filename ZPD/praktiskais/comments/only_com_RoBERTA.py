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

class overall:
    def calculate_sentiment():
        with open('praktiskais\comments\jsons\sentiment.json', 'r') as file:
            sentiment_data = json.load(file)

        highest_positive_values = []
        highest_neutral_values = []
        highest_negative_values = []

        for entry in sentiment_data:
            max_sentiment = max(entry, key=lambda k: entry[k] if k != 'text' else 0)

            if max_sentiment == 'positive':
                highest_positive_values.append(entry[max_sentiment])
            if max_sentiment == 'neutral':
                highest_neutral_values.append(entry[max_sentiment])
            if max_sentiment == 'negative':
                highest_negative_values.append(entry[max_sentiment])

        if highest_positive_values:
            average_highest_positive = sum(highest_positive_values) / len(highest_positive_values)
        else:
            average_highest_positive = 0

        if highest_neutral_values:
            average_highest_neutral = sum(highest_neutral_values) / len(highest_neutral_values)
        else:
            average_highest_neutral = 0

        if highest_negative_values:
            average_highest_negative = sum(highest_negative_values) / len(highest_negative_values)
        else:
            average_highest_negative = 0


        labels_counts = {
            'positive': len(highest_positive_values),
            'neutral': len(highest_neutral_values),
            'negative': len(highest_negative_values)
        }

        max_label = max(labels_counts, key=labels_counts.get)
        max_count = labels_counts[max_label]

        overall_sentiment = max(average_highest_positive, average_highest_neutral, average_highest_negative)


        if overall_sentiment == average_highest_positive:
            sentiment_label = 'positive'
        elif overall_sentiment == average_highest_neutral:
            sentiment_label = 'neutral'
        else:
            sentiment_label = 'negative'


        if sentiment_label == 'positive':
            sentiment_count = len(highest_positive_values)
        elif sentiment_label == 'neutral':
            sentiment_count = len(highest_neutral_values)
        else:
            sentiment_count = len(highest_negative_values)


        print(f'Total highest positive values: {sum(highest_positive_values)}')
        print(f'Number of highest positive entries: {len(highest_positive_values)}')
        print(f'Average highest positive value: {average_highest_positive}\n')

        print(f'Total highest neutral values: {sum(highest_neutral_values)}')
        print(f'Number of highest neutral entries: {len(highest_neutral_values)}')
        print(f'Average highest neutral value: {average_highest_neutral}\n')

        print(f'Total highest negative values: {sum(highest_negative_values)}')
        print(f'Number of highest negative entries: {len(highest_negative_values)}')
        print(f'Average highest negative value: {average_highest_negative}\n')

        comments = [entry['text'] for entry in sentiment_data]

        total_comment_count = len(comments)
        com_multy = (max_count/total_comment_count)*100
        portion_of_com = round(com_multy, 2)

        portion_of_com_positive = round(len(highest_positive_values)/total_comment_count, 2)
        portion_of_com_neutral = round(len(highest_neutral_values)/total_comment_count, 2)
        portion_of_com_negative = round(len(highest_negative_values)/total_comment_count, 2)

        print(f'on its own - Sentiment of the video is {max_label}: {portion_of_com}%\n')


        print(f'Sentiment of the video for positive: {portion_of_com_positive}%')

        print(f'Sentiment of the video for neutral: {portion_of_com_neutral}%')

        print(f'Sentiment of the video for negative: {portion_of_com_negative}%')

        highest_positive_comments = []
        highest_neutral_comments = []
        highest_negative_comments = []

        for entry in sentiment_data:
            max_sentiment = max(entry, key=lambda k: entry[k] if k != 'text' else 0)

            if max_sentiment == 'positive':
                highest_positive_comments.append({"text": entry['text']})
            if max_sentiment == 'neutral':
                highest_neutral_comments.append({"text": entry['text']})
            if max_sentiment == 'negative':
                highest_negative_comments.append({"text": entry['text']})

        with open('praktiskais/sentiment/positive.json', 'w') as file:
            json.dump(highest_positive_comments, file, indent=4)

        with open('praktiskais/sentiment/neutral.json', 'w') as file:
            json.dump(highest_neutral_comments, file, indent=4)

        with open('praktiskais/sentiment/negative.json', 'w') as file:
            json.dump(highest_negative_comments, file, indent=4)

# developer_key = "AIzaSyBrlZLMhq1thWEuGp6bxQufQka7fUUj9b4"
# video_id = "SzXOq1Q1J1Y"
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

sentiment_overall = overall()
overall.calculate_sentiment()
print("done!")