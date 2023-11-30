import json

file_path = 'praktiskais\\sentiment\\negative.json'

with open(file_path, 'r') as file:
    data = json.load(file)

for item in data:
    print(item["text"] + "\n")
