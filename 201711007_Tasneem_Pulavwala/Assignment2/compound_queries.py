import csv
from pprint import pprint
from elasticsearch import Elasticsearch

es = Elasticsearch()

# Compound Query - more than one query, matches using boolean
# combination of queries
# must, should, must_not, filter
pprint(es.search(index="books", doc_type="book", body={"query": {"bool":\
    {"must": { "match":{"title":"Rio"} },"must_not": { "range": {"price": \
    {"gte":"10","lte":"20"}}}}}}))
