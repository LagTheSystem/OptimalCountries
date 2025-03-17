import json

# Define the file paths
json_path = "./filtered_country_data.json"
js_path = "./site/country_data.js"
sorted_js_path = "./site/country_data.js"

# Initialize File
with open(json_path, "r", encoding="utf-8") as file:
    json_data = file.read()

# Parse the JSON data
data_array = json.loads(json_data)

# Sort the array alphabetically by the "country" key
sorted_data = sorted(data_array, key=lambda x: x["country"])

# Convert back to a JavaScript array
sorted_json_data = json.dumps(sorted_data, indent=2)
sorted_content = "const data = " + sorted_json_data
sorted_content += "\nexport default data;"

# Save the sorted data back to a new file
with open(sorted_js_path, "w", encoding="utf-8") as sorted_file:
    sorted_file.write(sorted_content)

