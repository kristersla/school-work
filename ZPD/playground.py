import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
import json

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyDULJIUW2H8ecxiZpPBfBobrImqMdbUMys"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)


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
                'replies': []  # Initialize replies list
            })

            if 'replies' in item:
                for reply_item in item['replies']['comments']:
                    reply = reply_item['snippet']
                    comments[-1]['replies'].append({  # Append replies to the last comment
                        'author': reply['authorDisplayName'],
                        'published_at': reply['publishedAt'],
                        'updated_at': reply['updatedAt'],
                        'like_count': reply['likeCount'],
                        'text': reply['textDisplay']
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


video_id = "Ljgk3lVvqyA"
comments = get_comments(video_id)

# Save to JSON file
with open('comments.json', 'w', encoding='utf-8') as f:
    json.dump(comments, f, ensure_ascii=False, indent=4)
    print("done!")
