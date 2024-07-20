# DecisionTreeClassifier
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error , mean_absolute_error
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.tree import export_graphviz
import graphviz

file = "breast-cancer-wisconsin.csv"
data = pd.read_csv(file)


# جدا کردن ویژگی‌ها و کلاس هدف
X = data.drop("Diagnosis", axis=1)
y = data["Diagnosis"]

# تقسیم مجموعه داده به مجموعه‌های آموزشی و آزمایشی
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ایجاد مدل درخت تصمیم
model = DecisionTreeClassifier(random_state=42)

# آموزش مدل بر روی مجموعه داده آموزشی
model.fit(X_train, y_train)

# پیش‌بینی‌ها را برای مجموعه داده آزمایشی انجام دهید
y_pred = model.predict(X_test)

# دقت مدل را محاسبه کنید
accuracy = accuracy_score(y_test, y_pred)
print("دقت:", accuracy)

# درخت تصمیم را به صورت بصری نشان دهید
text_representation = tree.export_text(model)
print (text_representation)


cols = ['Diagnosis','Radius_mean','Texture_mean','Perimeter_mean'
        ,'Area_mean','Smoothness_mean','Compactness_mean','Concavity_mean'
        ,'Nconcave_mean','Symmetry_mean','Fractaldim_mean','Radius_se'
        ,'Texture_se','Perimeter_se,Area_se','Smoothness_se','Compactness_se'
        ,'Concavity_se','Nconcave_se','Symmetry_se','Fractaldim_se','Radius_extreme'
        ,'Texture_extreme','Perimeter_extreme','Area_extreme','Smoothness_extreme'
        ,'Compactness_extreme','Concavity_extreme','Nconcave_extreme'
        ,'Symmetry_extreme','Fractaldim_extreme']
        
dot_data = export_graphviz(model , out_file = None
                           ,feature_names = cols , precision = 1
                           , filled = True , rounded = True
                           , special_characters = True)

graph = graphviz.Source(dot_data)
graph.render(view=True)






















