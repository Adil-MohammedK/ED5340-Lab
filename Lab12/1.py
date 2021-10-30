from sklearn.linear_model import LogisticRegression
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    precision_score,
    recall_score,
    roc_curve,
    auc,
    classification_report,
)

# In[4]
my_data = pd.read_csv("Logistic_regression_ls.csv")
X = np.ones((len(my_data), 2))
X[:, 0] = my_data.x1
X[:, 1] = my_data.x2
y = my_data.label
x_train, x_test, y_train, y_test = train_test_split(X, y, train_size=0.7)

# In[5]

clf = LogisticRegression().fit(x_train, y_train)
print("Coefficients: ", clf.coef_)
print("Intercepts: ", clf.intercept_)

# print(clf.predict(x_test))
y_pred = clf.predict(x_test)
# print(clf.predict_proba(x_test))

y_score = clf.predict_proba(
    x_test,
)[:, 1]
# In[6]
# Confusion Matrix
cm = confusion_matrix(y_test, y_pred, normalize="all", labels=clf.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
disp.plot()
plt.show()
precision = precision_score(y_test, y_pred)
f1_score = f1_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
fpr, tpr, thresholds = roc_curve(y_test, y_score)
area_under_curve = auc(fpr, tpr)
print("Precision: ", precision)
print("F1 Score: ", f1_score)
print("Recall: ", recall)
print("Area Under Curve: ", area_under_curve)
print("tpr:", tpr)
print("fpr:", fpr)


plt.plot(fpr, tpr, label="ROC curve (area = %0.2f)" % area_under_curve)
target_names = ["class 0", "class 1"]
print(classification_report(y_test, y_pred, target_names=target_names))
plt.show()

# In[7]
