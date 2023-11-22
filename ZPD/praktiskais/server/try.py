# read_json.py

import json

# Read the JSON file
with open("praktiskais\server\youtube_id.json", "r") as json_file:
    data = json.load(json_file)

# Extract the YouTube ID from the data
youtube_id = data["youtube_id"]

# Print the YouTube ID
print(f"The YouTube ID is: {youtube_id}")
