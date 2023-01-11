import pandas as pd

name = "botometer-feedback-2019"
# name = "gilani-2017"

# 提取数据
df = pd.read_csv("merged/" + name + '_final.csv')

label = df["type"].values
data = df.drop(columns=["type"], axis=1, inplace=False).values

print(data)
print(type(data))
print(len(data))