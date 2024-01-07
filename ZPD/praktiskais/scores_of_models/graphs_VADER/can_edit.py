from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import csv
import re

def clean(comment):
    comment = re.sub(r'http\S+', '', comment)
    comment = re.sub(r'[^a-zA-Z\s]', '', comment)
    comment = re.sub(r'@\w+', ' ', comment)
    comment = re.sub(r'<href+', '', comment)
    comment = re.sub(r'(\s+)', ' ', comment)
    comment = re.sub(r'\[[^]]*\]', ' ', comment)
    return comment.lower()

with open("praktiskais\\scores_of_models\\database.csv", newline='') as f:
    reader = csv.reader(f)
    next(reader, None)
    rows = list(reader)

sid = SentimentIntensityAnalyzer()

actual_labels = []
predicted_labels = []

for row in rows:
    comment = row[0]
    actual_label = row[1]
    comment = clean(comment)
    sentiment = sid.polarity_scores(comment)['compound']
    if sentiment >= 0.05:
        predicted_label = 'Positive'
    elif sentiment <= -0.05:
        predicted_label = 'Negative'
    else:
        predicted_label = 'Neutral'
    actual_labels.append(actual_label)
    predicted_labels.append(predicted_label)
    print(f"Comment: {comment} | Actual: {actual_label} | Predicted: {predicted_label}")

accuracy = accuracy_score(actual_labels, predicted_labels) * 100
precision = precision_score(actual_labels, predicted_labels, average='weighted', zero_division=1) * 100
recall = recall_score(actual_labels, predicted_labels, average='weighted', zero_division=1) * 100
f1 = f1_score(actual_labels, predicted_labels, average='weighted', zero_division=1) * 100

overall = (accuracy + precision + recall + f1) / 4

print(f"\nAccuracy: {accuracy:.2f}%")
print(f"Precision: {precision:.2f}%")
print(f"Recall: {recall:.2f}%")
print(f"F1 Score: {f1:.2f}%\n")
print(f"Kopuma: {overall:.2f}%")

# with open("praktiskais\\scores_of_models\\jsons\\VADER.json", "w") as f:
#     json.dump({"Accuracy": accuracy, "Precision": precision, "Recall": recall, "F1 Score": f1, "Overall score": overall}, f)
