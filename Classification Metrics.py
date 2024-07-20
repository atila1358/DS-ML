# Accurcy
from sklearn.metrics import accuracy_score

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 1, 2, 0, 1, 2]

accuracy = accuracy_score(y_true, y_pred)
print(accuracy)

# precision

from sklearn.metrics import precision_score

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 1, 2, 0, 1, 1]

precision = precision_score(y_true, y_pred)
print(precision)


# Recall
from sklearn.metrics import recall_score

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 1, 2, 0, 1, 1]

recall = recall_score(y_true, y_pred)
print(recall)


# F1 Score
from sklearn.metrics import f1_score

y_true = [0, 1, 0, 1, 0]
y_pred = [0, 1, 1, 0, 1]

# وزن پیش فرض (1 برای هر دو precision و recall)
f1 = f1_score(y_true, y_pred)
print(f1)

# beta = 2, recall دو برابر precision اهمیت دارد
f1_beta2 = f1_score(y_true, y_pred, beta=2)
print(f1_beta2)

# beta = 0.5, precision دو برابر recall اهمیت دارد
f1_beta05 = f1_score(y_true, y_pred, beta=0.5)
print(f1_beta05)


# AUC-ROC 
from sklearn.metrics import roc_auc_score

y_true = [0, 1, 0, 1, 0]
y_pred = [0.2, 0.8, 0.3, 0.9, 0.1]

# محاسبه AUC با آستانه پیش فرض
auc_default = roc_auc_score(y_true, y_pred)
print(auc_default)

# محاسبه AUC با آستانه های خاص
fpr = [0.1, 0.2, 0.3, 0.4, 0.5]
auc_fpr = roc_auc_score(y_true, y_pred, fpr=fpr)
print(auc_fpr)



# (Confusion Matrix)
from sklearn.metrics import confusion_matrix

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 1, 2, 0, 1, 1]

confusion = confusion_matrix(y_true, y_pred)
print(confusion)


    
