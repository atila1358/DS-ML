import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import silhouette_score

# بارگذاری مجموعه داده Iris از کتابخانه scikit-learn
data = pd.read_csv('iris.csv')

# انتخاب ویژگی ها
X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

# تقسیم داده ها به 80% آموزشی و 20% آزمایشی
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# ایجاد مدل جنگل تصادفی با 100 درخت
model = RandomForestClassifier(n_estimators=100, random_state=42)

# آموزش مدل با استفاده از داده های آموزشی
model.fit(X_train)

# پیش بینی خوشه ها برای داده های آزمایشی
y_pred = model.predict(X_test)

# محاسبه شاخص Silhouette برای ارزیابی کیفیت خوشه بندی
silhouette_avg = silhouette_score(X_test, y_pred)
print("شاخص Silhouette:", silhouette_avg)
