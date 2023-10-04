from langdetect import detect
import json

with open('praktiskais/comments.json', 'r', encoding='utf-8') as f:
    comments = json.load(f)

comments_not_in_english = []
replies_not_in_english = []

for comment in comments:
    text = comment.get("text") 
    if text and len(text) > 4:
        try:
            language = detect(text)
            if language != "en":
                comments_not_in_english.append({"text": text, "language": language})
        except Exception as e:
            print(f"An error occurred, empty 'text' list in comments.json ")

for comment in comments:
    replies = comment.get("replies")
    if replies:
        for reply in replies:
            if len(reply) > 4:
                try:
                    language = detect(reply)
                    if language != "en":
                        replies_not_in_english.append({"reply": reply, "language": language})  # Corrected key to "reply"
                except Exception as e:
                    print(f"An error occurred, empty 'replies' list in comments.json ")

if not comments_not_in_english:
    print("All comments are in English")
else:
    with open('praktiskais/comments_not_in_eng.json', 'w', encoding='utf-8') as f:
        json.dump(comments_not_in_english, f, ensure_ascii=False, indent=4)

if not replies_not_in_english:
    print("All replies are in English")
else:
    with open('praktiskais/replies_not_in_eng.json', 'w', encoding='utf-8') as f:
        json.dump(replies_not_in_english, f, ensure_ascii=False, indent=4)

print("done!")
