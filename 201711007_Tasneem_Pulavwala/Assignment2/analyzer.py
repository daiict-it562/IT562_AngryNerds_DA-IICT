import csv
from pprint import pprint
from elasticsearch import Elasticsearch

es = Elasticsearch()

#Define analyzer when creating index
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
            },
            "settings":{
              "analysis": {
                  "analyzer": {
                    "book_analyzer": {
                      "tokenizer": "book_tokenizer"
                    }
                  },
                  "tokenizer": {
                    "book_tokenizer": {
                      "type": "standard",
                      "max_token_length": 5
                    }
                }
            }
            }
        }))

#Standard Analyzer - used by default
pprint(es.indices.analyze(index="books", body={\
  "analyzer": "simple",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}))

#Simple Analyzer - breaks text whenever it encounters a non alphabet. tokenizer is lowercase
pprint(es.indices.analyze(index="books", body={\
  "analyzer": "simple",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}))

#Whitespace Analyzer
pprint(es.indices.analyze(index="books", body={\
  "analyzer": "whitespace",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}))

#Stop Analyzer - same as simple but can be used to remove stopwords
pprint(es.indices.analyze(index="books", body={\
  "analyzer": "stop",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}))

#Keyword Analyzer - returns entire input string as a single token
pprint(es.indices.analyze(index="books", body={\
  "analyzer": "keyword",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}))

#Pattern Analyzer - returns entire input string as a single token
pprint(es.indices.analyze(index="books", body={\
  "analyzer": "pattern",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}))

#Custom Anaylzer
pprint(es.indices.put_settings(index="books",body={\
    "analysis":{
        "analyzer":{
            "books_analyzer":{
                "tokenizer":"standard",
                
            }
        }
    }
}))
