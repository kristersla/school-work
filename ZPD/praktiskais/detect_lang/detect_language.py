from langdetect import detect
import json

with open('praktiskais/mix_C&R/mix_C&R.json', 'r', encoding='utf-8') as f:
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
    with open('praktiskais/detect_lang/only_english.json', 'w', encoding='utf-8') as f:
        json.dump(comments_in_english, f, ensure_ascii=False, indent=4)

if comments_not_in_english:
    with open('praktiskais/detect_lang/comments_not_in_eng.json', 'w', encoding='utf-8') as f:
        json.dump(comments_not_in_english, f, ensure_ascii=False, indent=4)

print("done!")
