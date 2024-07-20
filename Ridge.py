#Ridge
import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# داده‌ها را بارگیری کنید
data = pd.read_csv("house-prices.csv")

# تبديل داده ها به آرايه و جداسازي ستون قيمت به عنوان متغير تارگت 
X = data[["SqFt", "Bedrooms", "Bathrooms",'Offers']].to_numpy()
y = data["Price"].to_numpy()

# مجموعه داده را به مجموعه‌های آموزشی و آزمایشی تقسیم کنید
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2
                                                    , random_state=42)
# مدل لاسو را آموزش ميدهيم
# مقدار آلفا يک مقداري است که بايد بصورت تجربي به دست آيد
model = Ridge(alpha=0.01)
model.fit(X_train, y_train)

# پیش‌بینی‌ها را انجام دهید
y_pred = model.predict(X_test)

# عملکرد مدل را ارزیابی کنید
# ارزيابي روي داده هاي تست انجام ميشود 
mae = mean_absolute_error(y_test, y_pred)
# خطا را نرمال کنید
mean_y = np.mean(y_test)
normalized_mae = mae / mean_y
# خطا را به درصد تبدیل کنید
percent_error = normalized_mae * 100
print("Percent Error:", percent_error)



