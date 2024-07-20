import pandas as pd
from matplotlib import pyplot as plt

# خواندن داده ها از CSV
df = pd.read_csv('sp500_data.csv')

# محاسبه ماتریس همبستگی
corr_matrix = df.iloc[: , 1:8].corr()

# استخراج اسامی سهام
labels = df.columns[1:8]

# رسم ماتریس همبستگی
plt.matshow(corr_matrix, cmap='coolwarm')

# تنظیم تیک ها و برچسب ها
plt.xticks(range(len(labels)), labels, rotation=45, ha='left')
plt.yticks(range(len(labels)), labels)

# نمایش نوار رنگی
plt.colorbar()

# نمایش نمودار
plt.show()

