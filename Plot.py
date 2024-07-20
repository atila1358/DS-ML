# Line
##import pandas as pd
##import matplotlib.pyplot as plt
##import numpy as np
### داده‌ها را به صورت یک DataFrame Pandas ایجاد کنید
##data = pd.DataFrame({
##    "State": ["CA", "NY", "FL", "TX"],
##    "Population": [39237975, 19453502, 21542223, 29538105]})
### جمعیت هر ایالت را به ترتیب حروف الفبا مرتب کنید
##data_sorted = data.sort_values(by=['State'])
### نمودار خطی را ایجاد کنید
##
##plt.plot(data_sorted.State, data_sorted.Population
##         , marker='o', linestyle='-', color='b')
##
##plt.xlabel("State")
##plt.ylabel("Population")
### چرخش برچسب‌های x به 45 درجه به سمت راست
##plt.xticks(rotation=45, ha='right')  
##
### نمودار را نمایش دهید
##plt.grid(True)  # اضافه کردن خطوط شبکه
##plt.tight_layout()
##plt.show()
##

## Pie
##import pandas as pd
##import matplotlib.pyplot as plt
##import numpy as np
## داده‌ها را به صورت یک DataFrame Pandas ایجاد کنید
##data = pd.DataFrame({
##    "State": ["CA", "NY", "FL", "TX"],
##    "Population": [39237975, 19453502, 21542223, 29538105]})
## نمودار خطی را ایجاد کنید
##
##plt.figure(figsize=(8, 8))  # تنظیم اندازه نمودار
##
##plt.pie(data['Population'], labels=data['State'], autopct="%1.1f%%")  # رسم نمودار دایره ای
##plt.title("USA States Population")  # عنوان نمودار
##
##plt.show()  # نمایش نمودار
##
##



# Scatter
##import pandas as pd
##import matplotlib.pyplot as plt
##import numpy as np
### داده‌ها را به صورت یک DataFrame Pandas ایجاد کنید
##
### ایالت ها
##states = ["CA", "NY", "FL", "TX", "PA", "IL", "OH", "GA", "NC", "MI"]
### جمعیت (2020)
##population = [39237975, 19453502, 21542223, 29538105, 18008802
##              , 12812508, 11799368, 10617423, 10439849, 10077331]
##
### مساحت (مایل مربع)
##area = [163696, 54556, 66538, 268596, 46055, 57914, 41299, 59429
##                                                , 53273, 58216]
### رسم نمودار پراکندگی
##plt.scatter(area, population, c=population, cmap="viridis", alpha=0.7)  
##
### اضافه کردن برچسب ها و عنوان
##plt.xlabel("Area")
##plt.ylabel("Population")
##plt.title("Population Density")
##
### افزودن نوار رنگی برای نشان دادن تراکم جمعیت
##plt.colorbar(label="Person Per Mile")
##
### نمایش نمودار
##plt.grid(True)  # اضافه کردن خطوط شبکه
##plt.show()



### Box plot
##import matplotlib.pyplot as plt
##import pandas as pd
### دیتاست را به صورت DataFrame ایجاد کنید
##data = {
##    "Company": ["A", "A", "A", "A", "A", "B", "B", "B", "B"
##                , "B", "C", "C", "C", "C", "C"],
##    
##    "Sales": [10000, 12000, 15000, 18000, 21000, 15000, 17000
##              , 19000, 21000, 23000, 20000, 22000, 24000, 26000, 28000]}
##df = pd.DataFrame(data)
##
##
##company = df['Company'].unique()
### j[0]=company and j[1]=Seals
##sales   = [[j[1] for j in df.values if j[0] == i] for i in company]
##
### رسم نمودار جعبه ای
##bp = plt.boxplot( sales,labels= company) 
##
### اضافه کردن عنوان و برچسب ها
##plt.title("Annual Sales by Company", fontsize=16)
##plt.xlabel("Company", fontsize=12)
##plt.ylabel("Sales", fontsize=12)
##
### تنظیم شبکه ها
##plt.grid(axis='y', linestyle='--', alpha=0.7)
##
### نمایش نمودار
##plt.tight_layout()
##plt.show()
##            

### Heat Plot
##
##import matplotlib.pyplot as plt
##import numpy as np
##
### دیتاست نمونه
##np.random.seed(10)
##data = np.random.randint(10000, 30000, (3, 5))
##company_names = ['Company A', 'Company B', 'Company C']
##year_labels = ['2018', '2019', '2020', '2021', '2022']
##
### رسم نمودار حرارتی
##plt.figure(figsize=(10, 6))
##plt.imshow(data, aspect='auto', cmap='viridis')
##
### اضافه کردن برچسب ها
##plt.xticks(np.arange(len(year_labels)), year_labels)
##plt.yticks(np.arange(len(company_names)), company_names)
##
### اضافه کردن نوار رنگی
##plt.colorbar(label='Sales')
##
### تنظیم عنوان و برچسب ها
##plt.title("Annual Sales by Company")
##plt.xlabel("Year", fontsize=12)
##plt.ylabel("Company", fontsize=12)
##
### نمایش نمودار
##plt.show()


### Histogram
##import matplotlib.pyplot as plt
##import numpy as np
##
### دیتاست نمونه
### اعداد تصادفی نرمال
##data = np.random.randn(1000)  
##
### رسم نمودار هیستوگرام
##plt.hist(data , bins = 40)
##
### تنظیم عنوان و برچسب ها
##plt.title("Histogram of Random Data")
##plt.xlabel("Value")
##plt.ylabel("Frequency")
##
### نمایش نمودار
##plt.show()

##import matplotlib.pyplot as plt
##import numpy as np
##
### دیتاست نمونه
##data = [1,2,3,4,8,6,5,7
##        ,3,4,7,9,1,3,5,7
##        ,8,9,4,5,6,7,5,6
##        ,7,8,9,10]
##
### رسم نمودار هیستوگرام
##plt.hist(data, bins=[1, 4, 5, 8])
##
### تنظیم عنوان و برچسب ها
##plt.title("Histogram of Discrete Data")
##plt.xlabel("Value")
##plt.ylabel("Frequency")
##
### نمایش نمودار
##plt.show()
##

# Hexbin Plot

##import pandas as pd
##from matplotlib import pyplot as plt
##
##df = pd.read_csv('kc_tax.csv')
##df = df.loc[(df.TaxAssessedValue < 750000)
##            & (df.SqFtTotLiving > 100)
##            & (df.SqFtTotLiving<3500) , : ]
##
### رسم نمودار
##plt.hexbin(df.SqFtTotLiving, df.TaxAssessedValue
##           , cmap='viridis'  , bins=100)
##
### تنظیم عنوان و برچسب ها
##plt.title("Hexbin Plot)")
##plt.xlabel("X")
##plt.ylabel("Y")
##
### نمایش نمودار
##plt.show()
##


# Histogram
##import matplotlib.pyplot as plt
##import numpy as np
##
### دیتاست نمونه
### اعداد تصادفی نرمال
##data = np.random.randn(1000)  
##
### رسم نمودار هیستوگرام
##plt.hist(data , bins = 40  )
##
### تنظیم عنوان و برچسب ها
##plt.title("Histogram of Random Data")
##plt.xlabel("Value")
##plt.ylabel("Frequency")

# نمایش نمودار
#plt.show()

##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##
### نمونه داده ها را ایجاد کنید
##data = np.random.rand(1000)
##
### یک DataFrame از داده ها ایجاد کنید
##df = pd.DataFrame(data)
##
### نمودار هیستوگرام با چگالی را رسم کنید
##plt.hist(df, density=False)
##plt.xlabel('مقادیر')
##plt.ylabel('چگالی احتمال')
##plt.title('نمودار هیستوگرام با چگالی')
##plt.show()
##
##

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# تعریف پارامترهای توزیع نرمال
mean = 5
std_dev = 2

# ایجاد آرایه داده ها
#x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 1000)

# محاسبه چگالی احتمال
#y = stats.norm.pdf(x, loc=mean, scale=std_dev)

### رسم نمودار خطی
##plt.plot(x, y, label='توزیع نرمال')
##
### اضافه کردن عنوان، برچسب ها و افسانه
##plt.title('نمودار چگالی احتمال توزیع نرمال')
##plt.xlabel('X')
##plt.ylabel('چگالی احتمال')
##plt.legend()
##
### نمایش نمودار
##plt.show()












