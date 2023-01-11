# logistics regression
import pandas as pd
from sklearn import linear_model
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, \
    cohen_kappa_score, roc_auc_score
from termcolor import colored as cl

# name = "botometer-feedback-2019"
name = "gilani-2017"

train = pd.read_csv('../merged/' + name + '_merge.csv')
train.drop(columns=['protected'], axis=1, inplace=True)
test = pd.read_csv('../dataset/test.csv')
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

train_data = train
ytrain = train_data['type'].values
xtrain = train_data.drop(labels=['type', 'nickname_length'], axis=1)
xtrain.rename(columns={'screenname_length': 'name_length'}, inplace=True)
ytest = test['label'].values
xtest = test.drop(labels=['label'], axis=1)

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
# cm = metrics.confusion_matrix(ytest, ypred, labels=[0, 1])
# # print(cm)
# Accuracy = metrics.accuracy_score(ytest, ypred)
# # accuracy = log_reg.score(xtest, ytest) accuracy计算方法二
# Precision = metrics.precision_score(ytest, ypred, pos_label=1)
# Recall = metrics.recall_score(ytest, ypred, pos_label=1)
# F1_score = metrics.f1_score(ytest, ypred, pos_label=1)
# Kappa = metrics.cohen_kappa_score(ytest, ypred)
# Roc_auc = metrics.roc_auc_score(ytest, ypred)

print(cl('Accuracy of the model is {:.2%}'.format((accuracy_score(ytest, ypred))), attrs=['bold']))
print(cl('F1-Score of the model is {:.2%}'.format(f1_score(ytest, ypred)), attrs=['bold']))
print(cl('PrecisionScore of the model is {:.2%}'.format(precision_score(ytest, ypred)), attrs=['bold']))
print(cl('RecallScore of the model is {:.2%}'.format(recall_score(ytest, ypred)), attrs=['bold']))
print(cl('ROC_AUC_SCORE of the model is {:.2%}'.format(roc_auc_score(ytest, ypred)), attrs=['bold']))
print(cl('CohenKappaScore of the model is {:.2%}'.format(cohen_kappa_score(ytest, ypred)), attrs=['bold']))
