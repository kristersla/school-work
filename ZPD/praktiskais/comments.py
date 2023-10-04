import googleapiclient.discovery
import json

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyDULJIUW2H8ecxiZpPBfBobrImqMdbUMys"

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

    with open('praktiskais/comments.json', 'w', encoding='utf-8') as f:
        json.dump(comments, f, ensure_ascii=False, indent=4)

video_id = "1tVvwMKD19Y"
save_comments_to_json(video_id)


with open('praktiskais/comments.json', 'r', encoding='utf-8') as f:
    comments = json.load(f)

total_text = len(comments)

def count_replies(comment):
    return len(comment['replies'])

total_replies = 0

for comment in comments:
    num_replies = count_replies(comment)
    total_replies += num_replies

total_comments = total_text+ total_replies
print(f"Comments: {total_comments}, Text: {total_text}, Replies: {total_replies}")