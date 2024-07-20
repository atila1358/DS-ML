##import numpy as np
##import scipy.stats as stats
##from matplotlib import pyplot as plt
##
##sample = np.array([139 ,158 ,131 ,189 ,184 ,163 ,157 ,168
##                   ,153 ,188 ,167 ,131 ,152 ,175 ,181 ,140
##                   ,131 ,170,134 ,135 ,182 ,154, 187 ,176
##                   , 150 ,150, 151, 183, 150, 176 ,152 ,146
##                   , 134, 186, 186 ,175, 148 ,169 ,188 ,154
##                   ,155 ,150, 155 ,184 ,184 ,182, 170 ,150
##                   , 138, 160])
##
##av = np.mean(sample)
### محاسبه چولگی
##skew = stats.skew(sample)
### چاپ نتیجه
##print("چولگی:", skew)
### محاسبه کشیدگی
##kurtosis = stats.kurtosis(sample)
### چاپ نتیجه
##print("کشیدگی:", kurtosis)
### Perform Jarque-Bera test
##statistic, pval = stats.jarque_bera(sample)
##print ('Jarque-Bera test \n',50*'-')
### Interpret results
##if pval > 0.05:
##    print("Distribution is normal (p-value:", pval, ")")
##else:
##    print("Distribution is not normal (p-value:", pval, ")")
##print()
##
### آزمون Shapiro-Wilk
##shapiro_test = stats.shapiro(sample)
### تفسیر نتایج
##print ('Shapiro-Wilk Test \n',50*'-')
##if shapiro_test[0] > 0.05:
##  print("Distribution is normal (p-value:", shapiro_test[1], ")")
##else:
##  print("Distribution is not normal (p-value:", shapiro_test[1], ")") 
##plt.hist(sample , bins  = 20 , width  = 2)
##plt.xlabel('Students Height')
##plt.ylabel('samples')
##plt.axvline(x=av, color='r', linestyle='dashed', linewidth=2, label='میانگین')
##plt.show()
##
##
##




# کتابخانه های مورد نیاز
import pandas as pd

# داده های نظرسنجی را در یک دیکشنری ذخیره کنید
data = {
    "خیلی راضی": 250,
    "راضی": 300,
    "معمولی": 200,
    "ناراضی": 150,
    "خیلی ناراضی": 100
}

# تبدیل دیکشنری به دیتافریم pandas
df = pd.DataFrame.from_dict(data, orient='index', columns=['تعداد'])

# محاسبه CDF
df['CDF'] = df['تعداد'].cumsum() / df['تعداد'].sum()

# سطح رضایت مورد نظر
level = "راضی"

# احتمال رضایت حداقل به اندازه سطح مورد نظر
probability = df.loc[level, 'CDF']

# نمایش نتیجه
print(f"احتمال اینکه یک مشتری از خرید خود حداقل \"{level}\" باشد: {probability:.2%}")
























##import scipy.stats as stats
##
### نمونه داده‌ها
##data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
##
### آزمون Shapiro-Wilk
##shapiro_test = stats.shapiro(data)
##
### تفسیر نتایج
##if shapiro_test[0] > 0.05:
##  print("توزیع نرمال است (p-value:", shapiro_test[1], ")")
##else:
##  print("توزیع نرمال نیست (p-value:", shapiro_test[1], ")")
##
##import scipy.stats as stats
##
### نمونه داده‌ها
##data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
##
### آزمون Shapiro-Wilk
##shapiro_test = stats.shapiro(data)
##
### تفسیر نتایج
##if shapiro_test[0] > 0.05:
##  print("توزیع نرمال است (p-value:", shapiro_test[1], ")")
##else:
##  print("توزیع نرمال نیست (p-value:", shapiro_test[1], ")")
##
##
##
##import numpy as np
##import scipy.stats as stats
##
### Sample data
##data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
##
### Perform Jarque-Bera test
##statistic, pval = stats.jarque_bera(data)
##
### Interpret results
##if pval > 0.05:
##    print("Distribution is normal (p-value:", pval, ")")
##else:
##    print("Distribution is not normal (p-value:", pval, ")")
##
##
