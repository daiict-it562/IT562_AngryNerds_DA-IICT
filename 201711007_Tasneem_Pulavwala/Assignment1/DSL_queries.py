import csv
from pprint import pprint
from elasticsearch import Elasticsearch

es = Elasticsearch()

# Returns all documents
pprint(es.search(index="books", doc_type="book", body={"query":{"match_all":{}}}))

# Search by matching exactly : returns all documents with author containing Tobit
pprint(es.search(index="books", doc_type="book", body={"query":{"match":\
    {"author":"Tobit"}}}))

# Search by matching exactly : returns all documents with author containing
# either Tobit or Davy
pprint(es.search(index="books", doc_type="book", body={"query":{"match":\
    {"author":"Tobit Davy"}}}))

# Search by matching phrase : returns documents with title containing
# the entire phrase
pprint(es.search(index="books", doc_type="book", body={"query":\
    {"match_phrase":{"title":"Beach Party"}}}))

# Search-as-you-Type
pprint(es.search(index="books", doc_type="book", body={"query":\
    {"match_phrase_prefix":{"title":"Legen"}}}))

#Multi - match query : Matches multiple fields for the query string
#(Here, the title field is 2 times more important than author field)
pprint(es.search(index="books", doc_type="book", body={"query":{"multi_match":\
    {"query":"Brown LLC","fields":["title^2","author"],"type":"phrase"}}}))

# Common terms query: frequently appearing terms are considered stopwords
pprint(es.search(index="books", doc_type="book", body={"query":{"common":\
    {"title":{"query":"Softening of the Egg","cutoff_frequency":0.0001}}}}))

# Query String query: parsing
pprint(es.search(index="books", doc_type="book", body={"query":{"query_string":\
    {"default_field":"title","query":"of AND the"}}}))

# Simple Query String query:
pprint(es.search(index="books", doc_type="book", body={"query":{\
    "simple_query_string":{"fields":["title"],"query":"of +-the"}}}))

# Term query : exact matching, usually used for structured data, not full text fields
pprint(es.search(index="books", doc_type="book", body={"query":{"term":\
    {"isbn":"037755401-4"}}}))

# Compound Query
pprint(es.search(index="books", doc_type="book", body={"query": {"bool":\
    {"must": { "match_all": {} },"filter": { "range": {"price": \
    {"gte":"10","lte":"20"}}}}}}))
