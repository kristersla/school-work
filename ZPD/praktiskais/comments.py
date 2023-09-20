import googleapiclient.discovery
from googleapiclient.discovery import build
import json

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyDULJIUW2H8ecxiZpPBfBobrImqMdbUMys"

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)

def get_replies(comment_id, token):
    replies_response = youtube.comments().list(
        part='snippet',
        maxResults=100,
        parentId=comment_id,
        pageToken=token
    ).execute()

    replies = []

    for reply in replies_response['items']:
        replies.append(reply['snippet']['textDisplay'])

    if replies_response.get("nextPageToken"):
        replies += get_replies(comment_id, replies_response['nextPageToken'])

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
                'replies': get_replies(item['id'], None)
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
        print("done!")


video_id = "IVZJC2ZPzqw"
save_comments_to_json(video_id)
