from sklearn.model_selection import cross_val_score
from sklearn.metrics import get_scorer_names
from sklearn import svm
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn import linear_model

# print(get_scorer_names())

scoring = 'roc_auc'
print(scoring)

name = "botometer-feedback-2019"
# name = "gilani-2017"

# 提取数据
df = pd.read_csv("merged/" + name + '_final.csv')

# 分离内容与标签
label = df["type"].values
data = df.drop(columns=["type"], axis=1, inplace=False).values

# 各种模型

'''
# 决策树
model = dtc(criterion='entropy', max_depth=6)
treescores = cross_val_score(model, X=data, y=label, cv=10, scoring=scoring)
print("决策树:\n", treescores)

# 随机森林
random_forest = RandomForestClassifier(n_estimators=500, random_state=10)
rfscores = cross_val_score(random_forest, X=data, y=label, cv=10, scoring=scoring)
print("随机森林:\n", rfscores)

# 朴素贝叶斯
nb = MultinomialNB()
nbscores = cross_val_score(nb, X=data, y=label, cv=10, scoring=scoring)
print("朴素贝叶斯:\n", nbscores)

# 逻辑回归
log_reg = linear_model.LogisticRegression(penalty="l2", C=1, solver="liblinear")
log_regscores = cross_val_score(log_reg, X=data, y=label, cv=10, scoring=scoring)
print("逻辑回归:\n", log_regscores)


# 支持向量机
clf = svm.SVC(kernel='linear', C=1)
clf.fit(X=data, y=label)
# svmscores = cross_val_score(clf, X=data, y=label, cv=10, scoring=scoring)
# print("支持向量机:\n", svmscores)
'''
# 分离内容与标签
label = df["type"].values
data = df.drop(columns=["type"], axis=1, inplace=False).values


# 求均值
def average(input_data: list):
    lens = len(input_data)
    sums = 0
    for i in input_data:
        sums += i

    return sums / lens


# 各种模型
# 支持向量机
'''clf = svm.SVC(kernel='linear', C=1)
svmscoresacc = cross_val_score(clf, X=data, y=label, cv=10, scoring='accuracy')
svmscorespre = cross_val_score(clf, X=data, y=label, cv=10, scoring='precision')
svmscoresrec = cross_val_score(clf, X=data, y=label, cv=10, scoring='recall')
svmscoresf1 = cross_val_score(clf, X=data, y=label, cv=10, scoring='f1')
svmscoresra = cross_val_score(clf, X=data, y=label, cv=10, scoring='roc_auc')
print("支持向量机准确率")
print("accuracy:",average(svmscoresacc)),print("precision:",average(svmscorespre))
print("recall:",average(svmscoresrec)),print("f1:",average(svmscoresf1)),print("roc:",average(svmscoresra))'''
# 决策树
model = dtc(criterion='entropy', max_depth=6)
treescoresacc = cross_val_score(model, X=data, y=label, cv=10, scoring='accuracy')
treescorespre = cross_val_score(model, X=data, y=label, cv=10, scoring='precision')
treescoresrec = cross_val_score(model, X=data, y=label, cv=10, scoring='recall')
treescoresf1 = cross_val_score(model, X=data, y=label, cv=10, scoring='f1')
treescoresra = cross_val_score(model, X=data, y=label, cv=10, scoring='roc_auc')
print("决策树准确率")
print("accuracy:", average(treescoresacc)), print("precision:", average(treescorespre))
print("recall:", average(treescoresrec)), print("f1:", average(treescoresf1)), print("roc:", average(treescoresra))
# 随机森林
random_forest = RandomForestClassifier(n_estimators=500, random_state=10)
rfscoresacc = cross_val_score(random_forest, X=data, y=label, cv=10, scoring='accuracy')
rfscorespre = cross_val_score(random_forest, X=data, y=label, cv=10, scoring='precision')
rfscoresrec = cross_val_score(random_forest, X=data, y=label, cv=10, scoring='recall')
rfscoresf1 = cross_val_score(random_forest, X=data, y=label, cv=10, scoring='f1')
rfscoresra = cross_val_score(random_forest, X=data, y=label, cv=10, scoring='roc_auc')
print("随机森林准确率")
print("accuracy:", average(rfscoresacc)), print("precision:", average(rfscorespre))
print("recall:", average(rfscoresrec)), print("f1：", average(rfscoresf1)), print("roc:", average(rfscoresra))
# 朴素贝叶斯
nb = MultinomialNB()
nbscoresacc = cross_val_score(nb, X=data, y=label, cv=10, scoring='accuracy')
nbscorespre = cross_val_score(nb, X=data, y=label, cv=10, scoring='precision')
nbscoresrec = cross_val_score(nb, X=data, y=label, cv=10, scoring='recall')
nbscoresf1 = cross_val_score(nb, X=data, y=label, cv=10, scoring='f1')
nbscoresra = cross_val_score(nb, X=data, y=label, cv=10, scoring='roc_auc')
print("朴素贝叶斯准确率")
print("accuracy:", average(nbscoresacc)), print("precision:", average(nbscorespre))
print("recall:", average(nbscoresrec)), print("f1:", average(nbscoresf1)), print("roc:", average(nbscoresra))
# 逻辑回归
log_reg = linear_model.LogisticRegression(penalty="l2", C=1, solver="liblinear")
log_regscoresacc = cross_val_score(log_reg, X=data, y=label, cv=10, scoring='accuracy')
log_regscorespre = cross_val_score(log_reg, X=data, y=label, cv=10, scoring='precision')
log_regscoresrec = cross_val_score(log_reg, X=data, y=label, cv=10, scoring='recall')
log_regscoresf1 = cross_val_score(log_reg, X=data, y=label, cv=10, scoring='f1')
log_regscoresra = cross_val_score(log_reg, X=data, y=label, cv=10, scoring='roc_auc')
print("逻辑回归准确率")
print("accuracy:", average(log_regscoresacc)), print("precision:", average(log_regscorespre))
print("recall:", average(log_regscoresrec)), print("f1:", average(log_regscoresf1)), print("roc:",
                                                                                           average(log_regscoresra))
