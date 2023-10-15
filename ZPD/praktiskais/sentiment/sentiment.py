import json

with open('praktiskais/comments.json', 'r', encoding='utf-8') as f:
    comments = json.load(f)

total_text = len(comments)

def count_replies(comment):
    return len(comment['replies'])

total_replies = 0

for comment in comments:
    num_replies = count_replies(comment)
    total_replies += num_replies
    print(f"{comment['text']}:    {comment['replies']}")
