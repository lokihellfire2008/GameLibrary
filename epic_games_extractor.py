# Original author lokihellfire2008 https://github.com/lokihellfire2008/GameLibrary

import base64
import csv
import json

# Open the base64-encoded file and read its contents.  The path will be relative to your EpicGamesLauncher install
with open('C:\ProgramData\Epic\EpicGamesLauncher\Data\Catalog\catcache.bin', 'r') as f:
    encoded_data = f.read()

# Decode the base64-encoded data
decoded_data = base64.b64decode(encoded_data)

# Convert the decoded data to a string
decoded_string = decoded_data.decode('utf-8')

# Load the string as a JSON object
json_data = json.loads(decoded_string)

# Filter out elements where the 'namespace' key is 'poodle'
filtered_data = [elem for elem in json_data if elem.get('namespace') not in ['poodle', 'fn']]

# Print the filtered data to the console
for elem in filtered_data:
    print(elem.get('title'))

# Write the filtered data to a CSV file with two columns, 'Platform' and 'Title'
with open('epic_game_library.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Platform', 'Title'])
    for elem in filtered_data:
        title = elem.get('title')
        writer.writerow(['Epic', title])