import matplotlib.pyplot as plt  # 可视化
import pandas as pd  # 数据处理
from sklearn.metrics import accuracy_score, \
    f1_score, precision_score, recall_score, roc_auc_score, \
    cohen_kappa_score  # 模型准确度
from sklearn.tree import DecisionTreeClassifier as dtc  # 树算法
from sklearn.tree import plot_tree  # 树图
from termcolor import colored as cl  # 文本自定义

# import numpy as np  # 使用数组

learn_input = pd.read_csv('train.csv')
learn_input.drop(columns=['id', 'spilt', 'protected'], axis=1, inplace=True)

test_input = pd.read_csv('test.csv')
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

# 设置自变量/因变量

x_learn = learn_input[
    [
        'followers_count',
        'following_count',
        'tweet_count',
        'listed_count',
        'has_profile_photo',
        'verified',
        'name_length',
    ]
].values

y_learn = learn_input['label'].values

x_test = test_input[
    [
        'followers_count',
        'following_count',
        'tweet_count',
        'listed_count',
        'has_profile_photo',
        'verified',
        'name_length',
    ]
].values

y_test = test_input['label'].values
#
# print(cl(f'X变量举例：{x_learn[:5]}'))
# print(cl(f'Y变量举例：{y_learn[:5]}'))


model = dtc(criterion='entropy', max_depth=6)
model.fit(x_learn, y_learn)

pred_model = model.predict(x_test)

# TODO : 对于test.csv，用不同样本数量/不同测试集进行验证

# for  i in range(5):


# TODO : 自动将结果数据进行处理并输出到txt文档内


output = [accuracy_score(y_test, pred_model),
          f1_score(y_test, pred_model),
          precision_score(y_test, pred_model),
          recall_score(y_test, pred_model),
          roc_auc_score(y_test, pred_model),
          cohen_kappa_score(y_test, pred_model)]

'''
print(cl('Accuracy of the model is {:.2%}'.format((accuracy_score(y_test, pred_model))), attrs=['bold']))
print(cl('F1-Score of the model is {:.2%}'.format(f1_score(y_test, pred_model)), attrs=['bold']))
print(cl('PrecisionScore of the model is {:.2%}'.format(precision_score(y_test, pred_model)), attrs=['bold']))
print(cl('RecallScore of the model is {:.2%}'.format(recall_score(y_test, pred_model)), attrs=['bold']))
print(cl('ROC_AUC_SCORE of the model is {:.2%}'.format(roc_auc_score(y_test, pred_model)), attrs=['bold']))
print(cl('CohenKappaScore of the model is {:.2%}'.format(cohen_kappa_score(y_test, pred_model)), attrs=['bold']))
'''

for i in output:
    print(f"{i:.3%}")

# pred_model = model.predict(x_learn)
# print(cl(f'Accuracy of the model is {(accuracy_score(y_learn, pred_model))}', attrs=['bold']))

feature_names = learn_input.columns[:7]
target_names = learn_input['label'].unique().tolist()

plot_tree(model,
          feature_names=feature_names,
          class_names=str(target_names),
          filled=True,
          rounded=True,
          fontsize=3)

plt.rcParams["font.family"] = 'WenQuanYi Micro Hei'
plt.savefig('tree_visualization.png', dpi=500)
