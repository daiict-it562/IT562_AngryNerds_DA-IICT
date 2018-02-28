import csv
import pandas as pd
import spacy
from elasticsearch import Elasticsearch
from spacy import displacy

es = Elasticsearch()

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
print('\n')
print("="*100)
print('\n')

print('Reading Dataset....')
df = pd.read_csv('dummy_data.csv')
temp = df['Title']

print('for "Title" field:')
print('TEXT','|','START','|','END','|','LABEL')
for ab in temp:
    doc = nlp(ab)
    for np in doc.ents:
         print(np.text, '|', np.start_char, '|', np.end_char, '|', np.label_)
