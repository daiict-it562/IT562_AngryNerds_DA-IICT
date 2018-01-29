import csv
from pprint import pprint
from elasticsearch import Elasticsearch

es = Elasticsearch()

#es.indices.delete('books')

if not es.indices.exists(index="books"):
    pprint(es.indices.create(index="books", body=\
    {
        "mappings":{
            "book":{
                "properties":{
                    "title":{"type":"text","index_options":"positions"},
                    "author":{"type":"text"},
                    "publisher":{"type":"text"},
                    "price":{"type":"double"},
                    "genre":{"type":"text"},
                    "isbn":{"type":"keyword"},
                    "publish_date":{"type":"date"}
                    }
                }
            }
        }))


# Read CSV file and create documents
with open('dummy_data.csv',encoding="utf-8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        pprint(es.index(index="books", doc_type="book", body=\
        {
            "title":row[1],
            "author":row[2],
            "publisher":row[3],
            "price":row[4],
            "genre":row[5],
            "isbn":row[6],
            "publish_date":row[7]
        }))
