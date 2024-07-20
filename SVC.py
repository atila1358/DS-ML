#SVM (Classification)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# بارگذاری مجموعه داده Iris
data = pd.read_csv('iris.csv')

# جدا کردن ویژگی‌ها و هدف
X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = data['species']

# تقسیم داده‌ها به مجموعه‌های آموزشی و آزمایشی
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ایجاد مدل SVM
model = SVC()

# آموزش مدل
model.fit(X_train, y_train)

# پیش‌بینی برای مجموعه داده آزمایشی
y_pred = model.predict(X_test)

# محاسبه دقت مدل
accuracy = accuracy_score(y_test, y_pred)
print("دقت مدل:", accuracy)
