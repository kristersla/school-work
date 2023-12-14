import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'praktiskais\\sentiment\\negative.json'

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

sorted_data = sorted(data, key=lambda item: item['like_count'], reverse=True)

for item in sorted_data:
    print(f"{item['author']}: '{item['text']}'")
    print(f"patīk: {str(item['like_count'])}"+ "\n")
