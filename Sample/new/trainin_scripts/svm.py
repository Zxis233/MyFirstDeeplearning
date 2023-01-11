import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.metrics import cohen_kappa_score
from sklearn import svm
from sklearn import preprocessing
from termcolor import colored as cl  # 文本自定义


def calculate_score(df1, df2):
    for i in df1.type.values:
        if i == 'bot':
            df1.type.replace(i, 1, inplace=True)
        elif i == 'human':
            df1.type.replace(i, 0, inplace=True)

    for j in df2.label.values:
        if j == 'bot':
            df2.label.replace(j, 1, inplace=True)
        elif j == 'human':
            df2.label.replace(j, 0, inplace=True)

    # 训练集赋值
    y_train = df1["type"].values
    x_train = df1.drop(columns=["type", "nickname_length"], axis=1, inplace=False).values
    x_train = preprocessing.scale(x_train)

    # 进行训练
    clf = svm.SVC(kernel='linear')  # 创造线性分类器对象
    clf.fit(x_train, y_train.reshape(-1, 1).ravel())  # 开始训练拟合

    # 利用test测试
    # test = df2.sample(n=200, axis=0)  # 每次随机取200个样本进行测试
    test = df2
    # 样本集赋值
    y_test = test["label"].values
    x_test = test.drop(columns=["id", "label", "spilt"], axis=1, inplace=False).values
    x_test = preprocessing.scale(x_test)

    # ERROR
    y_pred = clf.predict(x_test).ravel()  # 预测并储存预测值
    y_true = y_test.ravel()

    # 计算acc，roc，kappa，f1，recall，precision
    ACC = accuracy_score(y_true, y_pred)
    Precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    F1_score = f1_score(y_true, y_pred)
    auc = roc_auc_score(y_true, y_pred)
    kappa = cohen_kappa_score(y_true, y_pred)

    # 设置返回值
    score = [ACC, F1_score, Precision, recall, auc, kappa]
    return score


# 读数据

# name = "botometer-feedback-2019"
name = "gilani-2017"

df1 = pd.read_csv("../merged/" + name + "_merge.csv")
df2 = pd.read_csv("../dataset/test.csv")

# 存数据
records = []
for i in range(0, 5):
    records.append(calculate_score(df1, df2))

# 平均值
ave = []
for i in range(0, 6):
    sum = 0
    for j in range(0, 5):
        sum = sum + records[j][i]
    ave.append(sum / 5)

# 合并数据
records.append(ave)

# 输出表格
out = pd.DataFrame.from_records(
    records,
    columns=[
        "acc", "F1-score", "precision", "ROC-AUC", "recall", "kappa",
    ],
    index=[
        "1", "2", "3", "4", "5", "average"
    ]
)

# out.to_csv(name+'_svm.csv')

# print(records)

print(cl('Accuracy of the model is {:.2%}'.format(records[0][0]), attrs=['bold']))
print(cl('F1-Score of the model is {:.2%}'.format(records[0][1]), attrs=['bold']))
print(cl('PrecisionScore of the model is {:.2%}'.format(records[0][2]), attrs=['bold']))
print(cl('RecallScore of the model is {:.2%}'.format(records[0][3]), attrs=['bold']))
print(cl('ROC_AUC_SCORE of the model is {:.2%}'.format(records[0][4]), attrs=['bold']))
print(cl('CohenKappaScore of the model is {:.2%}'.format(records[0][5]), attrs=['bold']))
