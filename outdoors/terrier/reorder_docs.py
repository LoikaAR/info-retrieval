import json

# Define your array of index numbers
docs = [13, 2, 700]  # Example array of index numbers

# Read the JSON file
with open('parsed.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Reorder the JSON entries based on the 'docs' array
ordered_data = [None]*len(docs)
for i in range(len(docs)):
    for j in range(len(data)):
        if (docs[i] == data[j]["docno"]):
            ordered_data[i] = data[j]

# print(data[1]["docno"])

# print(ordered_data)

# Rewrite the JSON file with ordered entries
with open('ordered_json_file.json', 'w', encoding='utf-8') as file:
    json.dump(ordered_data, file, indent=4, default=str)

