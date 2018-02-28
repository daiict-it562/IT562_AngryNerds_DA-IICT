import csv
import pandas as pd
import spacy
from elasticsearch import Elasticsearch

es = Elasticsearch()

print("Noun Chunks")
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Autonomous cars shift insurance liability toward manufacturers')
for chunk in doc.noun_chunks:
    print(chunk.text)
print('\n')
print("="*100)
print('\n')

print('Reading Dataset.....')
df = pd.read_csv('dummy_data.csv')

temp1 = df['Title']
print('for "Title" field:')
for ab1 in temp1:
    doc1 = nlp(ab1)
    for np1 in doc1.noun_chunks:
        print(np1.text)
