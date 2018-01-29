import csv
from pprint import pprint
from elasticsearch import Elasticsearch

es = Elasticsearch()

# Minimum Should Match - the minimum no of optional clauses that should match
pprint(es.search(index="books", doc_type="book", body={"query": {"bool":{\
        "minimum_should_match":1,
        "should": [
            {"match":{"title":"Rio"}},
            {"match":{"title":"2"}},
                ],
        "must": {
                "range": {
                    "price": {"gte":"10","lte":"20"}
                    }
                }}}}))
