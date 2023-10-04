from googletrans import Translator
import json

with open('praktiskais/detect_lang/comments_not_in_eng.json', 'r', encoding='utf-8') as f:
    comments_data = json.load(f)

translator = Translator()

translated_comments = []
for comment in comments_data:
    translated_text = translator.translate(comment['text'], src=comment['language'], dest='en')
    translated_comments.append({'text': translated_text.text})

translated_data = translated_comments
with open('praktiskais/translation/translated.json', 'w', encoding='utf-8') as f:
    json.dump(translated_data, f, indent=4)

print("translated!")