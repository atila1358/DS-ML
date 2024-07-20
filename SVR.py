#SVR (Regression)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# بارگذاری مجموعه داده
data = pd.read_csv('house-prices.csv')

# انتخاب ویژگی‌ها و هدف
X = data[['SqFt', 'Bedrooms', 'Bathrooms']]
y = data['Price']

# استانداردسازی ویژگی‌ها
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# تقسیم داده‌ها به مجموعه‌های آموزشی و آزمایشی
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y
                                                    , test_size=0.2
                                                    , random_state=42)

# ایجاد مدل SVR
model = SVR(kernel='rbf', gamma='auto')

# آموزش مدل
model.fit(X_train, y_train)

# پیش‌بینی برای مجموعه داده آزمایشی
y_pred = model.predict(X_test)

# محاسبه خطای میانگین مربعات (MSE)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("RMSE:", rmse)

