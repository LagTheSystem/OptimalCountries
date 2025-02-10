import json

with open('filtered_country_data.json', 'r') as file:
    data = json.load(file)

for i in range(len(data)):
    if "literacy_rate" in data[i]:
        continue
    else:
        print(data[i]["Country"])