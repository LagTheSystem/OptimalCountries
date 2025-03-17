import json

with open('filtered_country_data.json', 'r') as file:
    data = json.load(file)

for i, entry in enumerate(data):
    if "literacy_rate" in entry:
        continue
    print(data[i]["Country"])
