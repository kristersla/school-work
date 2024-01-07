import urllib.request
import csv
import numpy as np
from scipy.special import softmax
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import seaborn as sns
import json
import matplotlib.pyplot as plt
import random
import re

class SentimentAnalyzer:
    MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
    LABEL_MAPPING_LINK = "https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/sentiment/mapping.txt"

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
        
        top_label = self.labels[ranking[0]]

        return top_label

    def analyze_sentiments_in_csv(self, csv_file, num_comments=10):
        actual_labels = []
        predicted_labels = []
        
        with open(csv_file, newline='') as f:
            reader = csv.DictReader(f)
            rows = random.sample(list(reader), num_comments)

            for row in rows:
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
    
analyzer = SentimentAnalyzer()
actual_labels, predicted_labels = analyzer.analyze_sentiments_in_csv("praktiskais/scores_of_models/testing-larger.csv", num_comments=20) #max 3535

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

with open("praktiskais\scores_of_models\jsons\RoBERTa.json", "w") as f:
    json.dump({"Accuracy": accuracy, "Precision":precision, "Recall":recall, "F1 Score":f1, "Overall score": overall}, f)

plt.figure(figsize=(10, 6))
for i, (actual, predicted) in enumerate(zip(actual_labels_lower, predicted_labels_lower)):
    plt.scatter(i, 0, color='green' if actual == predicted else 'red', marker='o', s=50)
    plt.text(i, 0.2, f"Actual: {actual}\nPredicted: {predicted}", fontsize=8, ha='center')

plt.title('Labels Matched with Each Comment')
plt.xlabel('Comment Index')
plt.yticks([])
plt.show()
