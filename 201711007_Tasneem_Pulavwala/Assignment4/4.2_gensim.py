import numpy as np
import pandas as pd
import csv
import sklearn.preprocessing as sk
from gensim.corpora import MmCorpus
from gensim.test.utils import get_tmpfile
import gensim
import gensim.models.lsimodel as ls
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
from sklearn.utils.extmath import randomized_svd

ratings_list = [i.strip().split(",") for i in open('rating_data.csv', 'r').readlines()]

ratings_df = pd.DataFrame(ratings_list, columns = ['UserID', 'BookID', 'Rating'], dtype = float)

ratings_df.head()
ratings_df.loc[:,'Rating'] = sk.minmax_scale( ratings_df.loc[:,'Rating'] )
R_df = ratings_df.pivot(index = 'UserID', columns ='BookID', values = 'Rating').fillna(0).to_sparse(fill_value=0)
R_df.head()

R = R_df.as_matrix()
if(np.isinf(R).all()==False):
    print("tr")
Z=gensim.matutils.Dense2Corpus(R, documents_columns=True)
print(Z)

lsi=ls.LsiModel(Z, num_topics=3)
print("The sigma matrix:")
print(lsi.projection.s)

print("The matrix U:")
print(lsi.projection.u)

print("The transpose of the matrix V")
V = gensim.matutils.corpus2dense(lsi[Z], len(lsi.projection.s)).T / lsi.projection.s
print(V)
