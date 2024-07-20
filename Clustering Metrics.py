# Silhouette 
from sklearn.metrics import silhouette_score

X = [[1, 2], [2, 1], [5, 4], [8, 5], [7, 6]]
labels = [1, 1, 2, 2, 2]

silhouette_avg = silhouette_score(X, labels)
print(silhouette_avg)

# Calinski-Harabasz Index
from sklearn.metrics import calinski_harabasz_score

X = [[1, 2], [2, 1], [5, 4], [8, 5], [7, 6]]
labels = [1, 1, 2, 2, 2]

calinski_harabasz_score = calinski_harabasz_score(X, labels)
print(calinski_harabasz_score)


# davies_bouldin_score
from sklearn.metrics import davies_bouldin_score

X = [[1, 2], [2, 1], [5, 4], [8, 5], [7, 6]]
labels = [1, 1, 2, 2, 2]

davies_bouldin_score = davies_bouldin_score(X, labels)
print(davies_bouldin_score)

#   ARI
from sklearn.metrics import adjusted_rand_score

X = [[1, 2], [2, 1], [5, 4], [8, 5], [7, 6]]
labels_true = [1, 1, 2, 2, 2]
labels_pred = [1, 2, 2, 1, 2]

ari = adjusted_rand_score(labels_true, labels_pred)
print(ari)

# Mutual information
from sklearn.metrics import mutual_info_score

X = [[1, 2], [2, 1], [5, 4], [8, 5], [7, 6]]
labels_true = [1, 1, 2, 2, 2]
labels_pred = [1, 2, 2, 1, 2]

mi = mutual_info_score(labels_true, labels_pred)
print(mi)

#Purity 
from sklearn.metrics import purity_score

X = [[1, 2], [2, 1], [5, 4], [8, 5], [7, 6]]
labels_true = [1, 1, 2, 2, 2]
labels_pred = [1, 2, 2, 1, 2]

purity = purity_score(labels_true, labels_pred)
print(purity)


# Fowlkes-Mallows Score
from sklearn.metrics import fowlkes_mallows_score

X = [[1, 2], [2, 1], [5, 4], [8, 5], [7, 6]]
labels_true = [1, 1, 2, 2, 2]
labels_pred = [1, 2, 2, 1, 2]

fm_score = fowlkes_mallows_score(labels_true, labels_pred)
print(fm_score)











