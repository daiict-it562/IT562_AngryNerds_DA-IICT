#201711010- Jainam Shah

from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data1", "timestamp": datetime.now()})
es.index(index="my-index", doc_type="test-type", id=43, body={"any": "data2", "timestamp": datetime.now()})
es.index(index="my-index", doc_type="test-type", id=44, body={"any": "data3", "timestamp": datetime.now()})

#printing document from known id value
res1=es.get(index="my-index", doc_type="test-type", id=42)
print(res1['_source'])

#printing all documents
res = es.search(index="my-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(any)s %(timestamp)s" % hit["_source"])

#printing specific document via keyword
res = es.search(index="my-index", body={"query": {"match": {"any":"data1"}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(any)s %(timestamp)s" % hit["_source"])