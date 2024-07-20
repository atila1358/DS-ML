# K-Mean
import pandas as pd
from sklearn.cluster import KMeans

# دیتاست را بارگیری کنید
data = pd.read_csv("Sample Dataset.csv")

# ستون‌هایی را که می‌خواهید خوشه‌بندی کنید انتخاب کنید
X = data[['A','B','C']]

# تعداد خوشه‌ها را تعیین کنید
k = 5

# مدل K-Means را آموزش دهید
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)

# برچسب خوشه را به دیتاست اضافه کنید
data["خوشه"] = kmeans.labels_

# دیتاست را با برچسب‌های خوشه چاپ کنید
print(data)



