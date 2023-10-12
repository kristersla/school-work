from pytube import extract

#Examples
url1='http://youtu.be/SA2iWivDJiE'




id=extract.video_id(url1)
print(id)