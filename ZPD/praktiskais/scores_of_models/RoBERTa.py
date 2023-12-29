import csv
from transformers import pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import re

classifier = pipeline("sentiment-analysis", model="siebert/sentiment-roberta-large-english")

with open("praktiskais\\scores_of_models\\database.csv", newline='') as f:
    reader = csv.reader(f)
    
    next(reader, None)

    actual_labels = []
    predicted_labels = []

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

        result = classifier(comment)
        predicted_label = result[0]['label'].upper()

        actual_labels.append(actual_label)
        predicted_labels.append(predicted_label)

        print(f"Comment: {comment} | Actual: {actual_label} | Predicted: {predicted_label}")

actual_labels = [label.upper() for label in actual_labels]

accuracy = accuracy_score(actual_labels, predicted_labels)
precision = precision_score(actual_labels, predicted_labels, average='weighted', zero_division=1)
recall = recall_score(actual_labels, predicted_labels, average='weighted', zero_division=1)
f1 = f1_score(actual_labels, predicted_labels, average='weighted', zero_division=1)

print(f"\nAccuracy: {accuracy * 100:.2f}%")
print(f"Precision: {precision * 100:.2f}%")
print(f"Recall: {recall * 100:.2f}%")
print(f"F1 Score: {f1 * 100:.2f}%")

cm = confusion_matrix(actual_labels, predicted_labels)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=['Negative', 'Neutral', 'Positive'], yticklabels=['Negative', 'Neutral', 'Positive'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')
plt.show()
