#KNN (Binary)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# بارگذاری داده‌ها
data = pd.read_csv('KNN1.csv')

# جدا کردن ویژگی‌ها و برچسب‌ها
X = data[['A', 'B']]
y = data['Label']

# تقسیم داده‌ها به مجموعه‌های آموزشی و تست
X_train, X_test, y_train, y_test = train_test_split(X, y
                                                    , test_size=0.2
                                                    , random_state=42)

# آموزش مدل KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# پیش‌بینی برای مجموعه داده تست
y_pred = knn.predict(X_test)

# ارزیابی دقت مدل
accuracy = accuracy_score(y_test, y_pred)
print("دقت مدل:", accuracy)
