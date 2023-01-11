# 朴素贝叶斯
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, \
    cohen_kappa_score, auc, roc_auc_score, roc_curve
import numpy as np
from termcolor import colored as cl  # 文本自定义

# name = "botometer-feedback-2019"
name = "gilani-2017"

train = pd.read_csv('../merged/' + name + '_merge.csv')
train.drop(columns=['protected', 'nickname_length'], axis=1, inplace=True)
train.rename(columns={'screenname_length': 'name_length'}, inplace=True)

test = pd.read_csv('../dataset/' + 'test.csv')
test.drop(columns=['id', 'spilt', 'protected'], axis=1, inplace=True)

for i in train.type.values:
    if i == 'bot':
        train.type.replace(i, 1, inplace=True)
    elif i == 'human':
        train.type.replace(i, 0, inplace=True)

for j in test.label.values:
    if j == 'bot':
        test.label.replace(j, 1, inplace=True)
    elif j == 'human':
        test.label.replace(j, 0, inplace=True)

x_train = train.drop(["type"], axis=1).values
y_train = train["type"].values

x_test = test.drop(["label"], axis=1).values
y_test = test["label"].values

nb = MultinomialNB()
nb.fit(x_train, y_train)
prediction = nb.predict(x_test)
matrix = confusion_matrix(y_test, prediction)

# accuracy = accuracy_score(y_test, prediction)
# precision = precision_score(y_test, prediction, labels=None)
# recall = recall_score(y_test, prediction, labels=None)
# f1 = f1_score(y_test, prediction, labels=None)
# kappa = cohen_kappa_score(y_test, prediction)
# AUC = roc_auc_score(y_test, prediction, labels=None)

print(cl('Accuracy of the model is {:.2%}'.format((accuracy_score(y_test, prediction))), attrs=['bold']))
print(cl('F1-Score of the model is {:.2%}'.format(f1_score(y_test, prediction)), attrs=['bold']))
print(cl('PrecisionScore of the model is {:.2%}'.format(precision_score(y_test, prediction)), attrs=['bold']))
print(cl('RecallScore of the model is {:.2%}'.format(recall_score(y_test, prediction)), attrs=['bold']))
print(cl('ROC_AUC_SCORE of the model is {:.2%}'.format(roc_auc_score(y_test, prediction)), attrs=['bold']))
print(cl('CohenKappaScore of the model is {:.2%}'.format(cohen_kappa_score(y_test, prediction)), attrs=['bold']))
