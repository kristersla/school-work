from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request
import json

# Preprocess text (username and link placeholders)


task = 'sentiment'
MODEL = f"cardiffnlp/twitter-roberta-base-{task}"

tokenizer = AutoTokenizer.from_pretrained(MODEL)

# download label mapping
labels = []
mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
with urllib.request.urlopen(mapping_link) as f:
    html = f.read().decode('utf-8').split("\n")
    csvreader = csv.reader(html, delimiter='\t')
    labels = [row[1] for row in csvreader if len(row) > 1]

# PT
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
sentiment_results = []
# Load the JSON file
with open('praktiskais/comments/jsons/translated.json', 'r') as json_file:
    data = json.load(json_file)

for item in data:
    text = item['text']
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    result_item = {"text": text}

    for i in range(scores.shape[0]):
        l = labels[ranking[i]]
        s = scores[ranking[i]]
        result_item[l] = np.round(float(s), 4)

    sentiment_results.append(result_item)

# Save the results to a JSON file with newlines
output_file = 'praktiskais/sentiment/sentiment.json'
with open(output_file, 'w') as json_output_file:
    json.dump(sentiment_results, json_output_file, indent=4, separators=(',', ': '))

with open(output_file, 'r') as json_file:
    sentiment_data = json.load(json_file)


