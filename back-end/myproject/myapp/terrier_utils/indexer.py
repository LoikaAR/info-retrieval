import ssl
import json 
import pyterrier as pt
import pandas as pd
from .reorder_docs import *

def generate_factory():
    print('INDEXING...')
    # fix the ssl issue
    ssl._create_default_https_context = ssl._create_unverified_context

    # convert json to dataframe
    docs_df = pd.read_json("../../outdoors/scraped_data/res.json")
    docs_df['duration'].fillna('n/a h', inplace=True)
    docs_df.insert(0, 'docno', '')
    docs_df.insert(1, 'text', '')
    docs_df.insert(2, 'relevance', '')

    # print options
    pd.set_option('display.max_rows', docs_df.shape[0]+1)
    pd.set_option('display.max_columns', 10)

    # process descriptions
    docno = ['d' + str(i) for i in range(docs_df.shape[0])]
    docs_df['docno'] = docno
    text = []
    for i in range(docs_df.shape[0]):
        docs_df.loc[i, "description"] = ' '.join(str(s) for s in docs_df.loc[i, "description"])
        text.append(docs_df.loc[i, 'name'] + ' ' + docs_df.loc[i, 'description'])
    docs_df['text'] = text

    # out = docs_df.to_json(orient='records', lines=True)
    
    # res = loads(out)
    jlist = docs_df.to_dict(orient='records')

    with open('./myapp/terrier_utils/parsed.json', 'w') as f:
        json.dump(jlist, f, indent=4)

    # initialize terrier
    if not pt.started():
        pt.init()

    indexer = pt.DFIndexer("./index", overwrite=True)

    index_ref = indexer.index(docs_df['text'], docs_df['docno'])
    index_ref.toString()

    index = pt.IndexFactory.of(index_ref)
    br = pt.BatchRetrieve(index, wmodel="BM25") # alternative models: "TF_IDF", "BM25"

    return br

def transorm_query(br, query):
    queries = pd.DataFrame([["q1", query]], columns=["qid", "query"])

    res_df = br.transform(queries)

    jsoned = res_df.to_dict(orient="records")
    # parsed = json.loads(jsoned)
    # json.dumps(parsed, indent=4)  

    with open('./myapp/terrier_utils/retrieved.json', 'w') as file:
        json.dump(jsoned, file, indent=4)

    parse_order()

generate_factory()