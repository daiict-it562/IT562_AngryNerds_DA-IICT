#201711010 Jainam Shah

import csv
import pandas as pd
import spacy
from elasticsearch import Elasticsearch

es = Elasticsearch()

# mapping = {
#     "book-map": {
#         "properties": {
#             "title": {"type": "keyword"},
#             "author": {"type": "keyword"},
#             "genere": {"type": "keyword "},
#             "sub-genere": {"type": "keyword"},
#             "pages": {"type": "integer"},
#             "publisher": {"type": "keyword"}
#         }
#     }
# }
#
# if not es.indices.exists("book"):
#     es.indices.create("book")
#     es.indices.put_mapping(index="book",doc_type="book-map",body=mapping)
#
# with open('E:\\Vandan\\DA-IICT\\Academic Docs\\Sem 2\\IT562\\Assignment 1\\books_new.csv') as csvfile:  #importing csv and index creation
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         es.index(index="book", doc_type="book-map", body={"title": row['Title'], "author": row['Author'], "genere": row['Genre'],  "sub-genere": row['SubGenre'], "pages": row['Pages'], "publisher": row['Publisher']})

nlp = spacy.load('en_core_web_sm')
print('simple example:')
doc = nlp(u'Autonomous cars shift insurance liability toward manufacturers')
for chunk in doc.noun_chunks:
    print(chunk.text)
print('\n')
print("="*100)
print('\n')

print('for book dataset:')
df = pd.read_csv('E:\\Vandan\\DA-IICT\\Academic Docs\\Sem 2\\IT562\\Assignment 1\\books_new.csv')

temp1 = df['Title']

#for Title
print('for "Title" field:')
#print('TEXT','|','ROOT_TEXT')
for ab1 in temp1:
    doc1 = nlp(ab1)
    #print(doc)
    for np1 in doc1.noun_chunks:
        print(np1.text)