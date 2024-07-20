# Stacking
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
# بارگیری مجموعه داده
data = fetch_california_housing()
# جدا کردن ویژگی ها و قیمت ها
X = data.data
y = data.target
# تقسیم داده ها به مجموعه آموزشی و آزمایشی
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2
                                                    , random_state=42)
# ایجاد مدل های پایه
model_ada = AdaBoostRegressor(n_estimators=100, random_state=42)
model_gb = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1
                                     , max_depth=3, random_state=42)
# آموزش مدل های پایه
model_ada.fit(X_train, y_train)
model_gb.fit(X_train, y_train)

# پیش بینی های مدل های پایه
y_pred_ada = model_ada.predict(X_test)
y_pred_gb = model_gb.predict(X_test)

# ایجاد مجموعه داده متا
X_meta = np.hstack([y_pred_ada.reshape(-1, 1), y_pred_gb.reshape(-1, 1)])
# ایجاد مدل متا
model_meta = LinearRegression()
# آموزش مدل متا
model_meta.fit(X_meta, y_test)
# پیش بینی نهایی
y_pred_meta = model_meta.predict(X_meta)
# محاسبه R2
r2 = r2_score(y_test, y_pred_meta)
print("R2:", r2)
# محاسبه MSE
mse = mean_squared_error(y_test, y_pred_meta)
print("MSE:", mse)

