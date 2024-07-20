# GradientBoostingRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error

# بارگیری مجموعه داده
data = fetch_california_housing()

# جدا کردن ویژگی ها و قیمت ها
X = data.data
y = data.target

# تقسیم داده ها به مجموعه آموزشی و آزمایشی
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2
                                                    , random_state=42)

# ایجاد مدل Gradient Boosting
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1
                                  , max_depth=3, random_state=42)

# آموزش مدل
model.fit(X_train, y_train)

# پیش بینی قیمت ها
y_pred = model.predict(X_test)

# محاسبه R2
r2 = r2_score(y_test, y_pred)
print("R2:", r2)

# محاسبه MSE
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)

