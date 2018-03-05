#201711010 Jainam Shah

import numpy as np
import pandas as pd
import csv
import gensim.models.lsimodel as ls
import sklearn.preprocessing as sk
import gensim
from gensim.corpora import MmCorpus
from gensim.test.utils import get_tmpfile
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
from sklearn.utils.extmath import randomized_svd


ratings_list = [i.strip().split(",") for i in open('ratings.csv', 'r').readlines()]


ratings_df = pd.DataFrame(ratings_list, columns = ['UserID', 'BookID', 'Rating'], dtype = float)

ratings_df.head()
ratings_df.loc[:,'Rating'] = sk.minmax_scale( ratings_df.loc[:,'Rating'] )
##print(ratings_df.loc[:,'Rating'])

R_df = ratings_df.pivot(index = 'UserID', columns ='BookID', values = 'Rating').fillna(0).to_sparse(fill_value=0)
R_df.head()

#print(max(R_df.loc[:,:]))

R = R_df.as_matrix()
if(np.isinf(R).all()==False):
    print("tr")
##print(np.isinf(R),np.isnan(R))

Z=gensim.matutils.Dense2Corpus(R, documents_columns=True)
print(Z)

##user_ratings_mean = np.mean(R, axis = 1)
#print(R.size)
lsi=ls.LsiModel(Z, num_topics=3)
print("Sigma")

print(lsi.projection.s)
print("U")

print(lsi.projection.u)
print("VT")
V = gensim.matutils.corpus2dense(lsi[Z], len(lsi.projection.s)).T / lsi.projection.s
print(V)
