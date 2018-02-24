#201711010 Jainam Shah

from __future__ import unicode_literals
import textacy
import csv
import pandas as pd
import spacy
from elasticsearch import Elasticsearch
import en_core_web_sm

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

# if not es.indices.exists("book"):
#     es.indices.create("book")
#     es.indices.put_mapping(index="book",doc_type="book-map",body=mapping)
#
# with open('E:\\Vandan\\DA-IICT\\Academic Docs\\Sem 2\\IT562\\Assignment 1\\books_new.csv') as csvfile:  #importing csv and index creation
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         es.index(index="book", doc_type="book-map", body={"title": row['Title'], "author": row['Author'], "genere": row['Genre'],  "sub-genere": row['SubGenre'], "pages": row['Pages'], "publisher": row['Publisher']})

nlp = spacy.load('en_core_web_sm')
print('for book dataset:')
df = pd.read_csv('E:\\Vandan\\DA-IICT\\Academic Docs\\Sem 2\\IT562\\Assignment 1\\books_new.csv')
#for Title
print('for "Title":')
temp = df['Title']
nlp = en_core_web_sm.load()
pattern = r'<VERB>?<ADV>*<VERB>+'
for ab in temp:
    doc = textacy.Doc(ab, lang='en_core_web_sm')
    lists = textacy.extract.pos_regex_matches(doc, pattern)
    for list in lists:
        print(list.text," -> ", list.lemma_)