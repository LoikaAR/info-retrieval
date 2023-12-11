import json
import pandas as pd

def parse_order():
    # load docs
    docs = []
    retrieved = open('./myapp/terrier_utils/retrieved.json', 'r')
    batch = json.load(retrieved)

    idx = 0
    while idx < len(batch):
        docs.append(batch[idx].get('docno'))
        idx += 1 

    # Read the JSON file
    with open('./myapp/terrier_utils/parsed.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Reorder the JSON entries based on the 'docs' array
    ordered_data = [None]*len(docs)
    for i in range(len(docs)):
        for j in range(len(data)):
            if (docs[i] == data[j]["docno"]):
                ordered_data[i] = data[j]

    # print(data)

    # print(ordered_data)

    # Rewrite the JSON file with ordered entries
    # with open('./myapp/terrier_utils/ordered_json_file.json', 'w', encoding='utf-8') as file:
    #     json.dump(ordered_data, file, indent=4, default=str)

    with open('../../front-end/public/ordered_json_file.json', 'w', encoding='utf-8') as file:
        json.dump(ordered_data, file, indent=4, default=str)

