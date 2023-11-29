import pyterrier as pt
import pandas as pd
import json
import ssl

# fix the ssl issue
ssl._create_default_https_context = ssl._create_unverified_context

# add doc nums to json
docno = 0
with open('../scraped_data/res.json', 'r+') as target:
    data = json.load(target)
    for elem in data:
        elem["docno"] = docno
        docno += 1
        # elem["description"] = " ".join(str(s) for s in elem["description"])
    newData = json.dumps(data, indent=4)
# print(newData)

with open('./parsed.json', 'w') as file:
    file.write(newData)

# initialize terrier
if not pt.started():
    pt.init()

docs_df = pd.read_json("./parsed.json")
docs_df['duration'].fillna('n/a h', inplace=True)

indexer = pt.DFIndexer("./index", overwrite=True)

index_ref = indexer.index(docs_df["name"],
                          docs_df["region"],
                          docs_df["category"],
                          docs_df["distance"],
                          docs_df["duration"],
                          docs_df["ascent"],
                          docs_df["link"],
                          docs_df["description"],
                          docs_df["docno"])

index_ref.toString()