import urllib.request
import csv
import numpy as np
from scipy.special import softmax
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import seaborn as sns
import matplotlib.pyplot as plt
import json
import re

class HybridSentimentAnalyzer:
    VADER_THRESHOLD = 0.05
    ROBERTA_WEIGHT = 0.8

    def __init__(self):

        self.vader_analyzer = SentimentIntensityAnalyzer()

        self.roberta_tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        self.roberta_model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        self.roberta_labels = self._download_label_mapping()

    def _download_label_mapping(self):
        labels = []
        with urllib.request.urlopen("https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/sentiment/mapping.txt") as f:
            html = f.read().decode('utf-8').split("\n")
            csvreader = csv.reader(html, delimiter='\t')
            labels = [row[1] for row in csvreader if len(row) > 1]
        return labels

    def analyze_sentiment(self, text):

        vader_score = self.vader_analyzer.polarity_scores(text)['compound']


        inputs = self.roberta_tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
        output = self.roberta_model(**inputs)
        scores = output.logits[0].detach().numpy()
        scores = softmax(scores)

        ranking = np.argsort(scores)
        ranking = ranking[::-1]

        top_label = self.roberta_labels[ranking[0]]

        hybrid_score = (self.ROBERTA_WEIGHT * scores[ranking[0]]) + ((1 - self.ROBERTA_WEIGHT) * vader_score)

        if hybrid_score >= self.VADER_THRESHOLD:
            final_label = top_label
        else:
            final_label = 'Neutral'

        return final_label

    def analyze_sentiments_in_csv(self, csv_file):
        actual_labels = []
        predicted_labels = []

        with open(csv_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:

                comment = row["Comment"]
                actual_label = row["Label"]

                comment = re.sub(r'http\S+', '', comment)

                comment = re.sub(r'[^a-zA-Z\s]', '', comment)
                
                comment = re.sub(r'@\w+', '', comment)

                comment = re.sub(r'<herf+', '', comment)

                comment = re.sub(r'(\s+)', ' ', comment)

                comment = re.sub(r'\[[^]]*\]', ' ', comment)

                comment = re.sub(r'[^\w]', ' ', comment)

                comment = comment.lower()

                if comment:
                    result_item = self.analyze_sentiment(comment)

                    actual_labels.append(actual_label)
                    predicted_labels.append(result_item)

                    print(f"{comment} | {actual_label} | {result_item}")

        return actual_labels, predicted_labels

hybrid_analyzer = HybridSentimentAnalyzer()

actual_labels, predicted_labels = hybrid_analyzer.analyze_sentiments_in_csv("praktiskais/scores_of_models/database.csv")

print("Actual Labels:", actual_labels)
print("Predicted Labels:", predicted_labels)

actual_labels_lower = [label.lower() for label in actual_labels]
predicted_labels_lower = [label.lower() for label in predicted_labels]

accuracy = (accuracy_score(actual_labels_lower, predicted_labels_lower)) * 100
precision = (precision_score(actual_labels_lower, predicted_labels_lower, average='weighted', zero_division=1)) * 100
recall = (recall_score(actual_labels_lower, predicted_labels_lower, average='weighted', zero_division=1)) * 100
f1 = (f1_score(actual_labels_lower, predicted_labels_lower, average='weighted', zero_division=1)) * 100

overall = (accuracy + precision + recall + f1)/4

print(f"\nAccuracy: {accuracy:.2f}%")
print(f"Precision: {precision:.2f}%")
print(f"Recall: {recall:.2f}%")
print(f"F1 Score: {f1:.2f}%\n")
print(f"Overall score: {overall:.2f}%")

with open("praktiskais\scores_of_models\jsons\Hybrid.json", "w") as f:
    json.dump({"Accuracy": accuracy, "Precision":precision, "Recall":recall, "F1 Score":f1, "Overall score": overall}, f)


unique_labels_lower = set(actual_labels_lower + predicted_labels_lower)

cm = confusion_matrix(actual_labels_lower, predicted_labels_lower, labels=list(unique_labels_lower))

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=list(unique_labels_lower), yticklabels=list(unique_labels_lower))
plt.title('Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('Actual Labels')
plt.show()
