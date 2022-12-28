import pandas as pd

# name = "botometer-feedback-2019"
name = "gilani-2017"

user_info = pd.read_csv(name + '_tweets.csv')
detector_info = pd.read_csv(name + '_detect.csv')

user_info = user_info.set_index('id')
detector_info = detector_info.set_index('id')

merge = pd.concat([user_info, detector_info], axis=1, join='inner')

merge.to_csv(name + '_merge.csv', index=False)
