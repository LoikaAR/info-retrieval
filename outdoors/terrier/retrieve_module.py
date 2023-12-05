import ssl
import codecs
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

# print options
pd.set_option('display.max_rows', docs_df.shape[0]+1)
pd.set_option('display.max_columns', 10)

docno = ['d' + str(i) for i in range(docs_df.shape[0])]
docs_df['docno'] = docno
text = []
for i in range(docs_df.shape[0]):
    docs_df.loc[i, "description"] = ' '.join(str(s) for s in docs_df.loc[i, "description"])
    text.append(docs_df.loc[i, 'name'] + ' ' + docs_df.loc[i, 'description'])
docs_df['text'] = text

out = docs_df.to_json(orient='records', lines=True)
# res = loads(out)
jlist = docs_df.to_dict(orient='records')

with open('./parsed.json', 'w') as f:
    json.dump(jlist, f, indent=4)

# initialize terrier
if not pt.started():
    pt.init()

indexer = pt.DFIndexer("./index", overwrite=True)

index_ref = indexer.index(docs_df['text'], docs_df['docno'])
index_ref.toString()

index = pt.IndexFactory.of(index_ref)
print(index.getCollectionStatistics().toString())

# print lexicon
# for kv in index.getLexicon():
#   print("%s  -> %s " % (kv.getKey(), kv.getValue().toString()  ))

# print term attributes
# for kv in index.getLexicon() :
#   print(kv.getKey())
#   print(index.getLexicon()[kv.getKey()].toString())
#   print('**************************************************')

# print postings
# word_ = 'hike'
# pointer = index.getLexicon()[word_]
# for posting in index.getInvertedIndex().getPostings(pointer):
#     print(posting.toString() + " doclen=%d" % posting.getDocumentLength())

br = pt.BatchRetrieve(index, wmodel="Tf") #Alternative Models: "TF_IDF", "BM25"
# print(br.search("hike"))

queries = pd.DataFrame([["q1", "mountain bike"], ["q2", "nature"], ["q3", "cycling"]], columns=["qid", "query"])
# print(br.transform(queries))
