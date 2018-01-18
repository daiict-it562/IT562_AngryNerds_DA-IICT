#201711013- THAKER VANDAN BHARAT
import csv
from elasticsearch import Elasticsearch

#mapping
mapping = {
    "book-map": {
        "properties": {
            "title": {"type": "keyword", "index_options": "offsets"},
            "author": {"type": "keyword"},
            "genere": {"type": "keyword "},
            "sub-genere": {"type": "keyword"},
            "pages": {"type": "integer"},
            "publisher": {"type": "keyword", "index_options": "freqs"}
        }
    }
}

es = Elasticsearch()

if not es.indices.exists("book"):
    es.indices.create("book")
    es.indices.put_mapping(index="book",doc_type="book-map",body=mapping)

with open('books_new.csv') as csvfile:  #importing csv and index creation
    reader = csv.DictReader(csvfile)
    for row in reader:
        es.index(index="book", doc_type="book-map", body={"title": row['Title'], "author": row['Author'], "genere": row['Genre'],  "sub-genere": row['SubGenre'], "pages": row['Pages'], "publisher": row['Publisher']})

res = es.search(index="book", body={"query": {"match_all": {}}})

print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(title)s %(author)s %(genere)s %(sub-genere)s %(pages)s %(publisher)s" % hit["_source"])
