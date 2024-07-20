# LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# بارگذاری مجموعه داده گل‌ها
data = pd.read_csv("iris.csv")

# تبدیل ویژگی‌ها و برچسب‌ها به آرایه‌های NumPy
X = data[["sepal_length", "sepal_width", "petal_length", "petal_width"]].to_numpy()
y = data["species"].to_numpy()

# تبدیل برچسب‌ها به مقادیر عددی
# 0 -> Setosa   1 --> Versicolor  2 --> Virginica
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# تقسیم داده‌ها به مجموعه‌های آموزشی و آزمایشی
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ایجاد و آموزش مدل رگرسیون لجستیک
model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
model.fit(X_train, y_train)

# پیش‌بینی برای مجموعه داده‌های آزمایشی
y_pred = model.predict(X_test)

# دادن سه نمونه و دريافت تخمين
lst = [[5.1,3.5,1.4,.2] , [4.9,3,1.4,.2],[5.4,3.9,1.7,.4]]
y_pred = model.predict(lst)



