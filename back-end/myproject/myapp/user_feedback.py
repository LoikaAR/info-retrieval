import json


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

def change_score(doc_name, feedback):
    with open('./myapp/terrier_utils/retrieved.json', 'r', encoding='utf-8') as file:
        terrier_data = json.load(file)
    
    for ter_obj in terrier_data:
        if find_docno(doc_name) == ter_obj["docno"]:
            if feedback == "Yes":
                ter_obj["score"] *= 4
            # if feedback == 'No':
            #     ter_obj["score"] *= 0.01
            if feedback == '':
                ter_obj["score"] /= 4

    # re-sort the retrieved.json so that the entries are ordered from highest score to lowest
    terrier_data.sort(key=lambda x: x['score'], reverse=True)
    
    # update the 'rank' field based on the sorted order from 0 to n, 0 having the highest score
    for idx, ter_obj in enumerate(terrier_data):
        ter_obj['rank'] = idx
    
    with open('./myapp/terrier_utils/retrieved.json', 'w', encoding='utf-8') as file:
        json.dump(terrier_data, file, indent=4, default=str)

# def reorder_retrieved():

# subsequently i need to call parse_order from reorder_docs
# a get request needs to be triggered by the post request in the front-end, just like during query submission
