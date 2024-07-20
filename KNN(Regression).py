#KNN (Regression)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

# بارگذاری مجموعه داده
data = pd.read_csv("house-prices.csv")

# جدا کردن ویژگی‌ها و هدف
X = data[["SqFt", "Bedrooms", "Bathrooms"]]
y = data["Price"]

# تقسیم داده‌ها به مجموعه‌های آموزشی و آزمایشی
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ایجاد مدل KNN
knn_regressor = KNeighborsRegressor(n_neighbors=5)

# آموزش مدل
knn_regressor.fit(X_train, y_train)

# پیش‌بینی قیمت خانه‌های جدید
y_pred = knn_regressor.predict(X_test)

# محاسبه خطای مطلق میانگین (MAE)
mae = mean_absolute_error(y_test, y_pred)
print("خطای مطلق میانگین:", mae)

