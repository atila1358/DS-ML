# Random Forest (Regression)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# بارگذاری مجموعه داده مسکن
data = pd.read_csv('house-prices.csv')

# جدا کردن ویژگی‌ها و هدف
X = data[['SqFt', 'Bedrooms', 'Bathrooms']]
y = data['Price']

# تقسیم داده‌ها به مجموعه‌های آموزشی و آزمایشی
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# آموزش مدل جنگل تصادفی
model = RandomForestRegressor()
model.fit(X_train, y_train)

# پیش‌بینی برای مجموعه داده آزمایشی
y_pred = model.predict(X_test)

# ارزیابی خطای مدل
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("خطای جذر میانگین مربعات (RMSE):", rmse)
