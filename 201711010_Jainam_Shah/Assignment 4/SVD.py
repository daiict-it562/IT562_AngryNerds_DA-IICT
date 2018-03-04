#201711010 Jainam Shah

from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
# X = sparse_random_matrix(10000, 10000, density=0.01, random_state=42)
X = sparse_random_matrix(10000, 10000)

print(X)

TruncatedSVD(algorithm='randomized', n_components=5, n_iter=7, random_state=42, tol=0.0)
svd = TruncatedSVD(n_components=5, n_iter=7, random_state=42)
svd.fit(X)

print(svd.explained_variance_ratio_)

print(svd.explained_variance_ratio_.sum())

print(svd.singular_values_)
