# ICA
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import FastICA
import matplotlib.pyplot as plt


# بارگیری دیتاست
data = pd.read_csv("breast-cancer-wisconsin.csv")

# بررسی مقادیر گمشده
#print(data.isnull().sum())

# حذف ردیف‌های دارای مقادیر گمشده
data.dropna(inplace=True)

# استانداردسازی مقادیر ویژگی‌ها
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data[data.columns[:-1]])

# آموزش مدل ICA
ica = FastICA(n_components=10)
ica_transformed = ica.fit_transform(data_scaled)

# ماتريس وزني موئلفه هاي مستقل
ica_components = ica.components_


# فرض کنید components_ در یک متغیر به نام ica_components ذخیره شده است
ica_components_df = pd.DataFrame(ica_components)
fig, ax = plt.subplots()
ax.pcolor(ica_components_df, vmin=0, vmax=1)

# تنظیمات نمودار (اختیاری)
ax.set_title('Thermal display of independent components')# نمایش حرارتی مؤلفه‌های مستقل
ax.set_xlabel('Main feature') # ويژگيهاي اصلي
ax.set_ylabel('Independent Component')# موئلفه هاي مستقل 

# نمایش نمودار
plt.show()
