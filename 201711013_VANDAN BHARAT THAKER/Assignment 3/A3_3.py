#201711013-THAKER VANDAN BHARAT
import csv
import pandas as pd
import spacy
from elasticsearch import Elasticsearch
from spacy import displacy

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
# with open('E:\\Vandan\\DA-IICT\\Academic Docs\\Sem 2\\IT562\\Assignmnp 1\\books_new.csv') as csvfile:  #importing csv and index creation
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         es.index(index="book", doc_type="book-map", body={"title": row['Title'], "author": row['Author'], "genere": row['Genre'],  "sub-genere": row['SubGenre'], "pages": row['Pages'], "publisher": row['Publisher']})

nlp = spacy.load('en_core_web_sm')
#simple example
print('Simple Example:')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
print('\n')
print("="*100)
print('\n')

#with book dataset
print('with book dataset')
df = pd.read_csv('E:\\Vandan\\DA-IICT\\Academic Docs\\Sem 2\\IT562\\Assignment 1\\books_new.csv')
temp = df['Title']

# for Title
print('for "Title" field:')
print('TEXT','|','START','|','END','|','LABEL')
for ab in temp:
    doc = nlp(ab)
    #print(doc)
    for np in doc.ents:
         print(np.text, '|', np.start_char, '|', np.end_char, '|', np.label_)
