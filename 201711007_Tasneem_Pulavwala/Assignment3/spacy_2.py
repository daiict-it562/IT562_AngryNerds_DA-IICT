from __future__ import unicode_literals
import textacy
import csv
import pandas as pd
import spacy
from elasticsearch import Elasticsearch
import en_core_web_sm

es = Elasticsearch()
nlp = spacy.load('en_core_web_sm')
print('Reading Dataset....')
df = pd.read_csv('dummy_data.csv')
temp = df['Title']
nlp = en_core_web_sm.load()
pattern = r'<VERB>?<ADV>*<VERB>+'
for ab in temp:
    doc = textacy.Doc(ab, lang='en_core_web_sm')
    lists = textacy.extract.pos_regex_matches(doc, pattern)
    for list in lists:
        print(list.text," -> ", list.lemma_)
