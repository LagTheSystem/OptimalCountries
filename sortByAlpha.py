# Thank you ChatGPT

import json

# Define the file path
file_path = "./site/country_data.js"

# Read the file content
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Extract the JSON data from the JavaScript file
json_data_start = content.find("[")
json_data_end = content.rfind("]") + 1
json_data = content[json_data_start:json_data_end]

# Parse the JSON data
data_array = json.loads(json_data)

# Sort the array alphabetically by the "country" key
sorted_data = sorted(data_array, key=lambda x: x["country"])

# Convert back to a JavaScript array format
sorted_json_data = json.dumps(sorted_data, indent=2)

# Reconstruct the JavaScript file with sorted data
sorted_content = content[:json_data_start] + sorted_json_data + content[json_data_end:]

# Save the sorted data back to a new file
sorted_file_path = "./site/country_data.js"
with open(sorted_file_path, "w", encoding="utf-8") as sorted_file:
    sorted_file.write(sorted_content)

