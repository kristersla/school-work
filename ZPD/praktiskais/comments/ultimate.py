import googleapiclient.discovery
import json
from langdetect import detect
from googletrans import Translator

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyC85sT-fXJhvgfTIwJrmutBi3k_4fEbxco"

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)

def get_replies(comment_id):
    replies = []

    next_page_token = None
    while True:
        replies_response = youtube.comments().list(
            part='snippet',
            maxResults=100,
            parentId=comment_id,
            pageToken=next_page_token
        ).execute()

        for reply in replies_response.get('items', []):
            replies.append(reply['snippet']['textDisplay'])

        next_page_token = replies_response.get("nextPageToken")
        if not next_page_token:
            break

    return replies

def get_comments(video_id, max_results=100):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results,
        textFormat='plainText'
    )

    comments = []

    while request is not None:
        response = request.execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append({
                'author': comment['authorDisplayName'],
                'published_at': comment['publishedAt'],
                'updated_at': comment['updatedAt'],
                'like_count': comment['likeCount'],
                'text': comment['textDisplay'],
                'replies': get_replies(item['id'])
            })

        if 'nextPageToken' in response:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=max_results,
                pageToken=response['nextPageToken'],
                textFormat='plainText'
            )
        else:
            request = None

    return comments

def save_comments_to_json(video_id):
    comments = get_comments(video_id)

    with open('praktiskais/comments/jsons/comments.json', 'w', encoding='utf-8') as f:
        json.dump(comments, f, ensure_ascii=False, indent=4)

video_id = "gwCD5971zlo"
save_comments_to_json(video_id)

with open('praktiskais/comments/jsons/comments.json', 'r', encoding='utf-8') as f:
    comments = json.load(f)

total_text = len(comments)

def count_replies(comment):
    return len(comment['replies'])

total_replies = 0

for comment in comments:
    num_replies = count_replies(comment)
    total_replies += num_replies

total_comments = total_text + total_replies

with open('praktiskais/comments/jsons/comments.json', 'r', encoding='utf-8') as f:
    comments_data = json.load(f)

output_data = []
for comment in comments_data:
    output_data.append({"text": comment["text"]})
    for reply in comment.get("replies", []):
        output_data.append({"text": reply})

with open('praktiskais/comments/jsons/mix_C&R.json', 'w', encoding='utf-8') as file:
    json.dump(output_data, file, indent=4, ensure_ascii=False)

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
        except Exception as e:
            print(f"An error occurred, empty 'text' list in comments.json")

if comments_in_english:
    with open('praktiskais/comments/jsons/only_english.json', 'w', encoding='utf-8') as f:
        json.dump(comments_in_english, f, ensure_ascii=False, indent=4)

if comments_not_in_english:
    with open('praktiskais/comments/jsons/comments_not_in_eng.json', 'w', encoding='utf-8') as f:
        json.dump(comments_not_in_english, f, ensure_ascii=False, indent=4)

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


print(f"Comments: {total_comments}, Text: {total_text}, Replies: {total_replies}")
print("translated!")