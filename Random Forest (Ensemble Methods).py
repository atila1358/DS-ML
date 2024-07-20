# Random Forest (Ensemble Methods)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# بارگیری مجموعه داده
data = pd.read_csv('house-prices.csv')

# انتخاب ویژگی‌ها و هدف
X = data[['SqFt', 'Bedrooms', 'Bathrooms']]
y = data['Price']

# تعداد مدل‌های پایه
n_models = 100
base_models = []

# ایجاد مدل جنگل تصادفی
for _ in range(n_models):
    # تقسیم داده‌ها به مجموعه‌های آموزشی و آزمایشی
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # ایجاد درخت تصمیم
    tree = DecisionTreeRegressor(random_state=42)

    # آموزش درخت تصمیم بر روی مجموعه آموزشی
    tree.fit(X_train, y_train)

    # پیش‌بینی قیمت مسکن بر روی مجموعه آزمایشی
    y_pred = tree.predict(X_test)

    # اضافه کردن درخت به لیست مدل‌های پایه
    base_models.append(tree)


    
# ایجاد مدل جنگل تصادفی
model = RandomForestRegressor(estimators=base_models, random_state=42)

# آموزش مدل
model.fit(X_train, y_train)

# پیش‌بینی قیمت مسکن
y_pred = model.predict(X_test)

# ارزیابی عملکرد
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"میانگین خطای مربعات: {mse:.2f}")
print(f"ریشه میانگین خطای مربعات: {rmse:.2f}")
r2 = r2_score(y_test, y_pred)
print(f"میزان تبیین R^2: {r2:.2f}")

# رسم پراکندگی
plt.scatter(y_test)
