import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import json
import re

with open("praktiskais\\scores_of_models\\testing-larger.csv", newline='') as f:
    reader = csv.reader(f)
    next(reader, None)

    sid = SentimentIntensityAnalyzer()
    actual_labels = []
    predicted_labels = []
    polarities = []

    for row in reader:
        comment = row[0]
        actual_label = row[1]

        comment = re.sub(r'http\S+', '', comment)
        comment = re.sub(r'[^a-zA-Z\s]', '', comment)
        comment = re.sub(r'@\w+', '', comment)
        comment = re.sub(r'<herf+', '', comment)
        comment = re.sub(r'(\s+)', ' ', comment)
        comment = re.sub(r'\[[^]]*\]', ' ', comment)
        comment = re.sub(r'[^\w]', ' ', comment)

        comment = comment.lower()
        sentiment = sid.polarity_scores(comment)['compound']

        if sentiment >= 0.05:
            predicted_label = 'Positive'
        elif sentiment <= -0.05:
            predicted_label = 'Negative'
        else:
            predicted_label = 'Neutral'

        actual_labels.append(actual_label)
        predicted_labels.append(predicted_label)
        polarities.append(sentiment)

        print(f"Comment: {comment} | Actual: {actual_label} | Predicted: {predicted_label} | Polarity: {sentiment}")

plt.scatter(range(len(polarities)), polarities, c=polarities, cmap='viridis', marker='o')
plt.title('VADER polaritātes izkliedes diagramma')
plt.xlabel('Komentāri')
plt.ylabel('Polaritāte')
plt.colorbar(label='Polaritāte')
plt.show()

accuracy = (accuracy_score(actual_labels, predicted_labels)) * 100
precision = (precision_score(actual_labels, predicted_labels, average='weighted', zero_division=1)) * 100
recall = (recall_score(actual_labels, predicted_labels, average='weighted', zero_division=1)) * 100
f1 = (f1_score(actual_labels, predicted_labels, average='weighted', zero_division=1)) * 100

overall = (accuracy + precision + recall + f1) / 4

print(f"\nAccuracy: {accuracy:.2f}%")
print(f"Precision: {precision:.2f}%")
print(f"Recall: {recall:.2f}%")
print(f"F1 Score: {f1:.2f}%\n")
print(f"Overall score: {overall:.2f}%")

with open("praktiskais\\scores_of_models\\jsons\\VADER.json", "w") as f:
    json.dump({"Accuracy": accuracy, "Precision": precision, "Recall": recall, "F1 Score": f1, "Overall score": overall}, f)
