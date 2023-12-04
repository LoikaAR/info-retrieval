import ssl
import json
import pyterrier as pt
import pandas as pd

# fix the ssl issue
ssl._create_default_https_context = ssl._create_unverified_context

# convert json to dataframe
docs_df = pd.read_json("../scraped_data/res.json")
docs_df['duration'].fillna('n/a h', inplace=True)
docs_df.insert(0, 'docno', '')
docs_df.insert(1, 'text', '')

pd.set_option('display.max_rows', docs_df.shape[0]+1)
pd.set_option('display.max_columns', 7)

text = []
docno = 1
for i in range(docs_df.shape[0]):
    docs_df.loc[i, 'docno'] = 'd'+str(docno)
    docno += 1
    docs_df.loc[i, "description"] = " ".join(str(s) for s in docs_df.loc[i, "description"])
    text.append(docs_df.loc[i, 'name'] + ' ' + docs_df.loc[i, 'description'])
docs_df['text'] = text

print(docs_df['docno'], docs_df['text'])


# add doc nums to json
# with open('../scraped_data/res.json', 'r') as target:
#     data = json.load(target)
#     for elem in data:
#         elem["docno"] = docno
#         docno += 1
#         elem['text'] = elem['name'] + ' ' + elem['description']
#     newData = json.dumps(data, indent=4)

# with open('./parsed.json', 'w') as file:
#     file.write(newData)


# initialize terrier
if not pt.started():
    pt.init()

indexer = pt.DFIndexer("./index", overwrite=True)

index_ref = indexer.index(docs_df['text'], docs_df['docno'])

index_ref.toString()