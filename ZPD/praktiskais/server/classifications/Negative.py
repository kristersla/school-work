import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

file_path = 'praktiskais\\sentiment\\negative.json'

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

for item in data:
    print(f"{item['author']}: '{item['text']}'")
    print(f"likes: {str(item['like_count'])}"+ "\n")
