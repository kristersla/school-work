import json
import matplotlib.pyplot as plt

# Load data from JSON files
with open("praktiskais/scores_of_models/jsons/RoBERTa.json", "r") as f:
    roberta = json.load(f)

with open("praktiskais/scores_of_models/jsons/VADER.json", "r") as f:
    vader = json.load(f)

# Extract scores
metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
roberta_scores = [roberta[metric] for metric in metrics]
vader_scores = [vader[metric] for metric in metrics]

# Create line plots
plt.plot(metrics, roberta_scores, marker='o', label='RoBERTa')
plt.plot(metrics, vader_scores, marker='o', label='VADER')

# Add labels, title, and legend
plt.xlabel('Metrics')
plt.ylabel('Scores')
plt.title('Comparison of VADER and RoBERTa Models')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
