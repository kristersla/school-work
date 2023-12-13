from transformers import AutoModelForSequenceClassification, AutoTokenizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator
from scipy.special import softmax
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, confusion_matrix
import googleapiclient.discovery
from langdetect import detect
from cleantext import clean
import json
import re

class SentimentModel:
    def __init__(self, model_name, tokenizer_name):
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    def classify_sentiment(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        outputs = self.model(**inputs)
        logits = outputs.logits
        probabilities = softmax(logits.detach().numpy(), axis=1)
        predicted_class = int(probabilities.argmax(axis=1)[0])
        return predicted_class

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

    INPUT_FILE = 'praktiskais/comments/jsons/translated.json'
    OUTPUT_POSITIVE_FILE = 'praktiskais/comments/jsons/positive.json'
    OUTPUT_NEUTRAL_FILE = 'praktiskais/comments/jsons/neutral.json'
    OUTPUT_NEGATIVE_FILE = 'praktiskais/comments/jsons/negative.json'

    def analyze_sentiment(self, text):
        analyzer = SentimentIntensityAnalyzer()
        sentiment = analyzer.polarity_scores(text)
        return sentiment

    def analyze_sentiments_in_json(self):
        with open(self.INPUT_FILE, 'r') as json_file:
            data = json.load(json_file)

        positive_entries = []
        neutral_entries = []
        negative_entries = []

        for entry in data:
            text = entry.get('text', '')
            if text:
                sentiment_scores = self.analyze_sentiment(text)
                if sentiment_scores['compound'] >= 0.05:
                    positive_entries.append(entry)
                elif sentiment_scores['compound'] <= -0.05:
                    negative_entries.append(entry)
                else:
                    neutral_entries.append(entry)

        with open(self.OUTPUT_POSITIVE_FILE, 'w') as file:
            json.dump(positive_entries, file, indent=4)

        with open(self.OUTPUT_NEUTRAL_FILE, 'w') as file:
            json.dump(neutral_entries, file, indent=4)

        with open(self.OUTPUT_NEGATIVE_FILE, 'w') as file:
            json.dump(negative_entries, file, indent=4)

        positive_count = len(positive_entries)
        neutral_count = len(neutral_entries)
        negative_count = len(negative_entries)

        total_entries = len(data)

        positive_percentage = (positive_count / total_entries) * 100
        neutral_percentage = (neutral_count / total_entries) * 100
        negative_percentage = (negative_count / total_entries) * 100

        print(f"Positive: {positive_percentage:.2f}%")
        print(f"Neutral: {neutral_percentage:.2f}%")
        print(f"Negative: {negative_percentage:.2f}%")
        print("Data saved successfully.")

# Initialize SentimentModel
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer_name = "nlptown/bert-base-multilingual-uncased-sentiment"
sentiment_model = SentimentModel(model_name, tokenizer_name)

developer_key = "AIzaSyBrlZLMhq1thWEuGp6bxQufQka7fUUj9b4"
video_id = "SzXOq1Q1J1Y"
print("loading...")
scrape = Scrape_Comments(developer_key)
scrape.get_comments(video_id)
scrape.save_comments_to_json('praktiskais/comments/jsons/comments.json')
scrape.count_comments()

combine = Combine()
combine.mix_Rep_and_com()

detect_lang = Detect_Language()
detect_lang.detect_lang()

print("started translating...")
translate_all = Translate_All_Comments()
translate_all.translate()
print("done!")

print("started sentiment...")

# Perform sentiment classification
with open('praktiskais/comments/jsons/translated.json', 'r', encoding='utf-8') as f:
    comments_data = json.load(f)

X = [comment['text'] for comment in comments_data]
y = [sentiment_model.classify_sentiment(text) for text in X]

# Split the data for cross-validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train your model (not included in this example, you may want to use a library like scikit-learn or transformers)

# Evaluate F1-Score
y_pred = [sentiment_model.classify_sentiment(text) for text in X_test]
f1 = f1_score(y_test, y_pred, average='weighted')
print(f"F1-Score: {f1}")

# Display Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Perform Cross-Validation (not included in this example)

print("done!")
