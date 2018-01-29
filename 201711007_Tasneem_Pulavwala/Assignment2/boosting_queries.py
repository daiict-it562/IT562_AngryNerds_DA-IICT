import csv
from pprint import pprint
from elasticsearch import Elasticsearch

es = Elasticsearch()

# Boosting Query - promote or demote a result, give negative boost
pprint(es.search(index="books", doc_type="book", body={\
    "query": {
        "boosting":{
            "positive": { "match":{"title":"Captain"} },
            "negative": { "term": {"title":"Rio 2"}},
            "negative_boost":0.5,
            }}
            }))
