### HMM

## آموزش به شيوه مجزا
##import numpy as np
##from hmmlearn import hmm
##import pandas as pd
##
### داده های حسگر شتاب سنج را از یک فایل CSV بارگیری کنید
##data = pd.read_csv('Activity.csv')
##
### داده ها را به سه مجموعه داده جداگانه برای هر فعالیت تقسیم کنید
##sitting_data = data[data['label'] == 0]
##walking_data = data[data['label'] == 1]
##running_data = data[data['label'] == 2]
##
##
##### مدل HMM را با استفاده از ماتریس های احتمالی تعریف کنید
##model = hmm.GaussianHMM(n_components=3)
##
##### ماتریس های احتمالی را با استفاده از داده های آموزشی تخمین بزنید
##model.fit(sitting_data.iloc[: ,1:3])
##model.fit(walking_data.iloc[: ,1:3])
##model.fit(running_data.iloc[: ,1:3])
##
##
### داده های حسگر شتاب سنج جدید را به عنوان یک آرایه NumPy تعریف کنید
##new_data = np.array([[1.0, 0.5], [2.0, 1.0], [3.0, 1.5]])
##
### فعالیت را با استفاده از مدل پیش بینی کنید
##activities = model.predict(new_data)
##
### فعالیت های پیش بینی شده را چاپ کنید
##print("فعالیت های پیش بینی شده:", activities)
##



# آموزش به شيوه يکپارچه
import numpy as np
import pandas as pd
from hmmlearn import hmm


# بارگیری داده های حسگر شتاب سنج
data = pd.read_csv('Activity.csv')

# تقسیم داده ها به مجموعه های داده جداگانه برای آموزش و تست
train_data = data.iloc[:80 , 1:3]
test_data = data.iloc[80: , 1:3]

# تعریف و آموزش مدل HMM
model = hmm.GaussianHMM(n_components=3)
model.fit(train_data)

# پیش بینی فعالیت برای داده های حسگر شتاب سنج جدید
new_data = np.array([[1.0, 0.5], [2.0, 1.0], [3.0, 1.5]])
activities = model.predict(new_data)

# چاپ فعالیت های پیش بینی شده
print("فعالیت های پیش بینی شده:", activities)


