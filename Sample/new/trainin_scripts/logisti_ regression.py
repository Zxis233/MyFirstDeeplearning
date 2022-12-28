# logistics regression
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics

train = pd.read_csv('train1.csv', low_memory=False)
'''
train.has_profile_photo = train.has_profile_photo.astype(str).map({'FALSE':0, 'TRUE':1}) 
train.verified = train.verified.astype(str).map({'FALSE':0, 'TRUE':1})
train.label = train.label.astype(str).map({'human':0, 'bot':1})
'''

test = pd.read_csv('test.csv', low_memory=False)
'''
test.has_profile_photo = test.has_profile_photo.astype(str).map({'FALSE':0, 'TRUE':1})
test.verified = test.verified.astype(str).map({'FALSE':0, 'TRUE':1})
test.label = test.label.astype(str).map({'human':0, 'bot':1})
'''

train_data = train.sample(n=500, replace=True, random_state=38, axis=0)
ytrain = train_data['label']
xtrain = train_data.drop(labels=['label', 'id'], axis=1)
ytest = test['label']
xtest = test.drop(labels=['label', 'id'], axis=1)

# 建模
log_reg = linear_model.LogisticRegression(penalty="l2", C=1, solver="liblinear")
log_reg.fit(xtrain, ytrain)

# 返回模型参数
# print(log_reg.intercept_, log_reg.coef_)
test_data_proba = log_reg.predict_proba(xtest)

# 模型预测
ypred = log_reg.predict(xtest)

# 预测结果统计
# print(pd.Series(log_reg).value_counts())

# 混淆矩阵
cm = metrics.confusion_matrix(ytest, ypred, labels=[0, 1])
# print(cm)
Accuracy = metrics.accuracy_score(ytest, ypred)
# accuracy = log_reg.score(xtest, ytest) accuracy计算方法二
Precision = metrics.precision_score(ytest, ypred, pos_label=1)
Recall = metrics.recall_score(ytest, ypred, pos_label=1)
F1_score = metrics.f1_score(ytest, ypred, pos_label=1)
Kappa = metrics.cohen_kappa_score(ytest, ypred)
Roc_auc = metrics.roc_auc_score(ytest, ypred)

print("test data Accuracy is :", Accuracy)
print("test data Precision is :", Precision)
print("test data Recall is :", Recall)
print("test data F1_score is :", F1_score)
print("test data Kappa is :", Kappa)
print("test data Roc_auc is :", Roc_auc)
