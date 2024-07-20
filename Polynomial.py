# PolynomialFeatures
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# فرض کنید فایل CSV شما "house_prices.csv" نام دارد و در پوشه فعلی شما قرار دارد
data = pd.read_csv("house-prices.csv")

# جدا کردن ویژگی‌ها (X) و متغیر وابسته (y)
X = data[["SqFt", "Bedrooms", "Bathrooms"]]
y = data["Price"]
# تنظیم درجه چندجمله‌ای
degree = 2

# ایجاد تبدیل کننده ویژگی‌های پلی‌نومال
poly_features = PolynomialFeatures(degree=degree, include_bias=False)

# تبدیل ویژگی‌ها به ویژگی‌های پلی‌نومال
X_poly = poly_features.fit_transform(X)

# ایجاد مدل رگرسیون خطی
model = LinearRegression()
model.fit(X_poly, y)
# پیش‌بینی قیمت مسکن
y_pred = model.predict(X_poly)


# محاسبه خطای میانگین مربعات (MSE)
mse = mean_squared_error(y, y_pred)
print("خطای میانگین مربعات:", mse)

# محاسبه ضریب تعیین (R^2)
r2 = r2_score(y, y_pred)
print("ضریب تعیین:", r2)


