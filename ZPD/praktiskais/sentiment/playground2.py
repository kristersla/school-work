import json

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

# Get the count for the relevant label
if sentiment_label == 'positive':
    sentiment_count = len(highest_positive_values)
elif sentiment_label == 'neutral':
    sentiment_count = len(highest_neutral_values)
else:
    sentiment_count = len(highest_negative_values)


# Print statistics for each sentiment type
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