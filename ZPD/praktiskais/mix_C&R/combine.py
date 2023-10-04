import json

with open('praktiskais/comments.json', 'r', encoding='utf-8') as file:
    comments_data = json.load(file)

output_data = []
for comment in comments_data:
    output_data.append({"text": comment["text"]})
    for reply in comment.get("replies", []):
        output_data.append({"text": reply})

with open('praktiskais/mix_C&R/mix_C&R.json', 'w', encoding='utf-8') as file:
    json.dump(output_data, file, indent=4, ensure_ascii=False)

print("mixed!")