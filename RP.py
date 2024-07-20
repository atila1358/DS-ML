# RP
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn import random_projection
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RandomizedProjection



# بارگیری دیتاست سرطان پستان
data = load_breast_cancer()
X = data.data  # ویژگی‌ها
y = data.target  # برچسب‌ها

# استانداردسازی ویژگی‌ها
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# کاهش بعد با RP
rp = RandomizedProjection(n_components=10)
X_rp = rp.fit_transform(X_scaled)

# بررسی شکل دیتاست
print("شکل دیتاست اصلی:", X.shape)
print("شکل دیتاست با RP:", X_rp.shape)

