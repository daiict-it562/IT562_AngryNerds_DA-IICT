import numpy as np
import pandas as pd
import csv
import sklearn.preprocessing as sk
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
from sklearn.utils.extmath import randomized_svd

ratings_list = [i.strip().split(",") for i in open('rating_data.csv', 'r').readlines()]
print(ratings_list)

ratings_df = pd.DataFrame(ratings_list, columns = ['UserID', 'BookID', 'Rating'], dtype = float)
print(ratings_df)

ratings_df.head()
ratings_df.loc[:,'Rating'] = sk.minmax_scale( ratings_df.loc[:,'Rating'] )
print(ratings_df.loc[:,'Rating'])

R_df = ratings_df.pivot(index = 'UserID', columns ='BookID', values = 'Rating').fillna(0)
R_df.head()
print(R_df)

R = R_df.as_matrix()
user_ratings_mean = np.mean(R, axis = 1)

R_demeaned = R - user_ratings_mean.reshape(-1, 1)
U, Sigma, VT = randomized_svd(R,n_components=2)

svd = TruncatedSVD(n_components=20, n_iter=7)
svd.fit(R)
print("The matrix U:")
print(U)
print("The sigma matrix:")
print(Sigma)
print("The matrix V (Transpose):")
print(VT)

print(svd.explained_variance_ratio_)
print(svd.components_)
print(svd.singular_values_)
