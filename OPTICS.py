import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import OPTICS
from sklearn.datasets import load_iris
from sklearn.metrics import adjusted_rand_score


# مجموعه داده Iris را بارگیری کنید
iris = load_iris()
data = iris.data
target = iris.target

# بارگذاری مجموعه داده گل‌ها
data = pd.read_csv("iris.csv")
df = data[["sepal_length", "sepal_width", "petal_length", "petal_width"]]

# م آموزش دهید
optics = OPTICS(min_samples=5 ,  eps = 0.5)

# خوشه ها را پیش بینی کنید
labels = optics.fit_predict(df)

data['cluster'] = labels
# نقشه رنگ را برای خوشه ها تعریف کنید
colors = ['green', 'blue', 'red']


# دقت خوشه بندی را با ARI محاسبه کنید
ari = adjusted_rand_score(data['species'], labels)

# نمودار پراکندگی را با افسانه رسم کنید
plt.scatter(df['sepal_length'], df['sepal_width'], c=labels, cmap='viridis', label=labels)

# برچسب ها و عنوان را اضافه کنید
plt.xlabel("طول کاسبرگ")
plt.ylabel("عرض کاسبرگ")
plt.title("خوشه بندی OPTICS با مجموعه داده Iris")
plt.show()
print(f"Adjusted Rand Index (ARI): {ari:.2f}")


