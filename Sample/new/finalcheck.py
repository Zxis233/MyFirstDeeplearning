import pandas as pd
from pandas import DataFrame

name = "botometer-feedback-2019"
# name = "gilani-2017"

origin_data: DataFrame | None = pd.read_csv("merged/" + name + "_merge.csv")

for i in origin_data.type.values:
    if i == 'bot':
        origin_data.type.replace(i, 1, inplace=True)
    elif i == 'human':
        origin_data.type.replace(i, 0, inplace=True)

for i in origin_data.has_profile_photo.values:
    if i == True:
        origin_data.has_profile_photo.replace(i, 1, inplace=True)
    elif i == False:
        origin_data.has_profile_photo.replace(i, 0, inplace=True)

for i in origin_data.protected.values:
    if i == True:
        origin_data.protected.replace(i, 1, inplace=True)
    elif i == False:
        origin_data.protected.replace(i, 0, inplace=True)

for i in origin_data.verified.values:
    if i == True:
        origin_data.verified.replace(i, 1, inplace=True)
    elif i == False:
        origin_data.verified.replace(i, 0, inplace=True)

# def replace_value(source: DataFrame, column, old_values: list, new_values: list):
#     ol = len(old_values)
#     nl = len(new_values)
#     if ol != nl:
#         print("元素个数不相等")
#         return
#
#     for i in source.column.values:
#         for j in range(ol):
#             if i == old_values[j]:
#                 source.column.type.repalce(i, new_values[j], inplace=True)
#                 continue
#     #
#     # return source


# replace_value(origin_data, type, ['bot', 'human'], [0, 1])

origin_data.to_csv("merged/" + name + "_final.csv", index=False)
