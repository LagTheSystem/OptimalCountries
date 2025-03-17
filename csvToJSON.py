import csv
import json

def csv_to_json(csv_file, json_file):
    data = []

    # Read CSV file
    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    # Write JSON file
    with open(json_file, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

# Example usage
csv_to_json('input.csv', 'output.json')
