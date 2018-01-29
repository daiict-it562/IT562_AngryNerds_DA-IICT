#Similarity --- Boost
import csv
from pprint import pprint
from elasticsearch import Elasticsearch

es = Elasticsearch()

pprint(es.indices.delete('*'))

# Creating index
# adding similarity to fields author and title
# title field is given boost 2 (twice as important as other fields)
if not es.indices.exists(index="books"):
    pprint(es.indices.create(index="books", body=\
    {
        "mappings":{
            "book":{
                "properties":{
                    "title":{"type":"text","index_options":"positions","similarity":"boolean","boost":2},
                    "author":{
                                "type":"text",
                                "similarity":"classic"
                              },
                    "publisher":{"type":"text"},
                    "price":{"type":"double"},
                    "genre":{"type":"text"},
                    "isbn":{"type":"keyword"},
                    "publish_date":{"type":"date"}
                    }
                }
            }
        }))
