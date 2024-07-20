from sklearn.metrics import accuracy_score

y_true = [0, 1, 2, 3, 4]
y_pred = [0, 0, 2, 3, 4]

accuracy = accuracy_score(y_true, y_pred)
print(accuracy)


from sklearn.metrics import classification_report

y_true = [0, 1, 2, 3, 4]
y_pred = [0, 0, 2, 3, 4]

print(classification_report(y_true, y_pred))


from sklearn.metrics import accuracy_score

y_true = [0, 1, 2, 3, 4]
y_pred = [0, 0, 2, 3, 4]

accuracy = accuracy_score(y_true, y_pred)
error = 1 - accuracy
print(error)





from sklearn.metrics import precision_score, recall_score, f1_score

y_true = [0, 1, 2, 3, 4]
y_pred = [0, 0, 2, 3, 4]

precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print(precision)
print(recall)
print(f1)


