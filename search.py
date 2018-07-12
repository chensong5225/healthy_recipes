from whoosh.qparser import *
from whoosh.fields import Schema,TEXT,STORED
from whoosh import index

schema = Schema(title = TEXT(stored=True),
                desc = TEXT(stored=True),
                ingredients = TEXT(stored=True),
                steps = TEXT(stored=True),
                reviews = TEXT(stored=True),
                tags = TEXT(stored=True))

ix = index.open_dir("indexdir2.0")
parser = QueryParser("ingredients",schema=schema)

def searching(q):
    result = parser.parse(q)
    titles = set()
    with ix.searcher() as searcher:
        results = searcher.search(result,limit=100)
        for r in results:
            titles.add(r['title'])
    return list(titles)

import pandas as pd
df = pd.read_csv('data/for_search.csv')

def reranking(title_list):
    result_list = pd.DataFrame(columns=df.columns.copy())
    for t in title_list:
        result_list = result_list.append(df[df['title']==t])
    r = result_list.sort_values(by=['RRR'],ascending=False)
    col = ['title', 'healthy', 'RRR', 'desc', 'ingredients', 'steps', 'tags']
    return r[col][:10].to_html(index=False)
