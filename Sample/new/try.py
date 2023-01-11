from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn import datasets
import pandas as pd

clf = svm.SVC(kernel='linear', C=1)
iris = datasets.load_iris()
scores = cross_val_score(clf, iris.data, iris.target, cv=5, scoring='f1_macro')
print(scores)

# print(iris.data)
# print(type(iris.data))
print(len(iris.data))