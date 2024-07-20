import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# بارگذاری مجموعه داده گل‌ها
data = pd.read_csv("iris.csv")
df = data[["sepal_length", "sepal_width", "petal_length", "petal_width"]]

# مدل DBSCAN را با پارامترهای eps و minPts آموزش دهید
dbscan = DBSCAN(eps=0.5, min_samples=5)

# خوشه ها را پیش بینی کنید
labels = dbscan.fit_predict(df)


# خوشه ها را در نمودار پراکندگی رسم کنید
plt.scatter(df['sepal_length'], df['sepal_width'], c=labels, cmap='viridis')
plt.xlabel("طول کاسبرگ")
plt.ylabel("عرض کاسبرگ")
plt.title("خوشه بندی DBSCAN با مجموعه داده Iris")

plt.show()
