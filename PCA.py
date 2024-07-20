# PCA
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# بارگیری دیتاست
data = pd.read_csv("breast-cancer-wisconsin.csv")

# بررسی مقادیر گمشده
print(data.isnull().sum())

# حذف ردیف‌های دارای مقادیر گمشده
data.dropna(inplace=True)

# تبدیل داده‌ها به نوع عددی
data["Diagnosis"] = data["Diagnosis"].map({"M": 1, "B": 0})

# استانداردسازی مقادیر ویژگی‌ها
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data[data.columns[1:]])

# آموزش مدل PCA
pca = PCA(n_components=0.95)
pca_transformed = pca.fit_transform(data_scaled)

# بررسی مؤلفه‌های اصلی
print(pca.explained_variance_ratio_)
print(pca.singular_values_)

# تبدیل داده‌ها به فضای جدید PCA
data_pca = pd.DataFrame(pca_transformed
                    , columns=["PC{}".format(i) for i in range(pca_transformed.shape[1])])

# ادغام داده‌ها با مؤلفه‌های PCA
data_with_pca = pd.concat([data, data_pca], axis=1)

# نمایش اطلاعات نهایی
print(data_with_pca.head())
