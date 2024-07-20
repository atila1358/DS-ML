# HC (Clustring)
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as sh
import matplotlib.pyplot as plt

#from scipy.cluster.hierarchy import linkage, dendrogram


# دیتاست CSV را بخوانید
data = pd.read_csv('Sample Dataset.csv')

# دیتاست را به آرایه NumPy تبدیل کنید
data_array = data.to_numpy()

# الگوریتم را با معیار پیوند تکمیل اجرا کنید
linkage = sh.linkage(data_array, method='complete')

# خوشه‌ها را با استفاده از آستانه 3.0 ایجاد کنید
cluster_labels = sh.fcluster(linkage, 3.0, criterion='distance')

# برچسب‌های خوشه را به دیتاست اضافه کنید
data['cluster'] = cluster_labels

print(data)
# ترسیم نمودار دندروگرام
sh.dendrogram(linkage)
plt.xlabel("Cluster")
plt.ylabel("Distance")
plt.title("Dendogram")
plt.show()

