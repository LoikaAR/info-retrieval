import json
from math import floor


def find_docno(name):
    docno = -1
    with open('../../front-end/public/ordered_json_file.json', 'r', encoding='utf-8') as file:
        dt = json.load(file)
    for obj in dt:
        if name == obj["name"]:
            docno = obj["docno"]
            break
    return docno


# def change_score(doc_name, feedback):
#     with open('./myapp/terrier_utils/retrieved.json', 'r', encoding='utf-8') as file:
#         terrier_data = json.load(file)
#     for ter_obj in terrier_data:
#         if find_docno(doc_name) == ter_obj["docno"]:
#             if feedback == "Yes":
#                 ter_obj["score"] *= 4
#             # if feedback == 'No':
#             #     ter_obj["score"] *= 0.01
#             if feedback == '':
#                 ter_obj["score"] /= 4

#     with open('./myapp/terrier_utils/retrieved.json', 'w', encoding='utf-8') as file:
#         json.dump(terrier_data, file, indent=4, default=str)

def update_relevance(docno, feedback):
    with open('./myapp/terrier_utils/parsed.json', 'r', encoding='utf-8') as file:
        dt = json.load(file)
    for obj in dt:
        if docno == obj["docno"]:
            obj["relevance"] = feedback
            print("object relevace: " + obj["relevance"])
            break
            
    with open('./myapp/terrier_utils/parsed.json', 'w', encoding='utf-8') as file:
        json.dump(dt, file, indent=4, default=str)



def reset_relevance():
    with open('./myapp/terrier_utils/parsed.json', 'r', encoding='utf-8') as file:
        dt = json.load(file)
    for obj in dt:
        obj["relevance"] = ''
    with open('./myapp/terrier_utils/parsed.json', 'w', encoding='utf-8') as file:
        json.dump(dt, file, indent=4, default=str)



def change_score(doc_name, feedback):
    with open('./myapp/terrier_utils/retrieved.json', 'r', encoding='utf-8') as file:
        terrier_data = json.load(file)
    
    for ter_obj in terrier_data:
        if find_docno(doc_name) == ter_obj["docno"]:
            update_relevance(find_docno(doc_name),feedback)
            # print(find_docno(doc_name))
            if feedback == "Yes":
                ter_obj["score"] *= 3
            if feedback == 'No':
                ter_obj["score"] *= 0.07
            if feedback == '':
                if floor(ter_obj["score"]) % 3 == 0:
                    ter_obj["score"] /= 3
                elif floor(ter_obj["score"]) % 0.07 == 0:
                    ter_obj["score"] /= 0.07
                

    # re-sort the retrieved.json so that the entries are ordered from highest score to lowest
    terrier_data.sort(key=lambda x: x['score'], reverse=True)
    
    # update the 'rank' field based on the sorted order from 0 to n, 0 having the highest score
    for idx, ter_obj in enumerate(terrier_data):
        ter_obj['rank'] = idx
    
    with open('./myapp/terrier_utils/retrieved.json', 'w', encoding='utf-8') as file:
        json.dump(terrier_data, file, indent=4, default=str)



def update_order():
    # load docs
    docs = []
    retrieved = open('./myapp/terrier_utils/retrieved.json', 'r')
    batch = json.load(retrieved)

    idx = 0
    while idx < len(batch):
        docs.append(batch[idx].get('docno'))
        idx += 1 

    # Read the JSON file
    with open('../../front-end/public/ordered_json_file.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Reorder the JSON entries based on the 'docs' array
    ordered_data = [None]*len(docs)
    for i in range(len(docs)):
        for j in range(len(data)):
            if (docs[i] == data[j]["docno"]):
                ordered_data[i] = data[j]

    with open('../../front-end/public/ordered_json_file.json', 'w', encoding='utf-8') as file:
        json.dump(ordered_data, file, indent=4, default=str)


# def reorder_retrieved():

# subsequently i need to call parse_order from reorder_docs
# a get request needs to be triggered by the post request in the front-end, just like during query submission
