from pathlib import Path
import numpy as np
import pandas as pd
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, matthews_corrcoef, auc, roc_curve, \
    roc_auc_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from termcolor import colored as cl  # 文本自定义

# name = "botometer-feedback-2019"
name = "gilani-2017"

learn_input = pd.read_csv('../merged/' + name + '_merge.csv')
learn_input.drop(columns=['protected'], axis=1, inplace=True)
learn_input.rename(columns={'screenname_length': 'name_length', 'type': 'label'}, inplace=True)

test_input = pd.read_csv('../dataset/' + 'test.csv')
test_input.drop(columns=['id', 'spilt', 'protected'], axis=1, inplace=True)

# 将标签改为0/1
for i in learn_input.label.values:
    if i == 'bot':
        learn_input.label.replace(i, 1, inplace=True)
    elif i == 'human':
        learn_input.label.replace(i, 0, inplace=True)

for j in test_input.label.values:
    if j == 'bot':
        test_input.label.replace(j, 1, inplace=True)
    elif j == 'human':
        test_input.label.replace(j, 0, inplace=True)

x_train = learn_input.drop(columns=["nickname_length", "label"]).values

y_train = learn_input["label"].values

x_test = test_input[
    [
        'followers_count',
        'following_count',
        'tweet_count',
        'listed_count',
        'time_to_now',
        'has_profile_photo',
        'verified',
        'name_length',
    ]
].values

y_test = test_input["label"].values

random_forest = RandomForestClassifier(class_weight='balanced', n_estimators=500, random_state=6)
random_forest.fit(x_train, y_train)
y_pred = random_forest.predict(x_test)
y_ture = y_test

print(cl('Accuracy of the model is {:.2%}'.format((accuracy_score(y_test, y_pred))), attrs=['bold']))
print(cl('F1-Score of the model is {:.2%}'.format(f1_score(y_test, y_pred)), attrs=['bold']))
print(cl('PrecisionScore of the model is {:.2%}'.format(precision_score(y_test, y_pred)), attrs=['bold']))
print(cl('RecallScore of the model is {:.2%}'.format(recall_score(y_test, y_pred)), attrs=['bold']))
print(cl('ROC_AUC_SCORE of the model is {:.2%}'.format(roc_auc_score(y_test, y_pred)), attrs=['bold']))
print(cl('CohenKappaScore of the model is {:.2%}'.format(cohen_kappa_score(y_test, y_pred)), attrs=['bold']))
