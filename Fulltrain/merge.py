import pandas as pd

# name = "botometer-feedback-2019"

user_info = pd.read_csv('all.csv')
tweet_info = pd.read_csv('csv/tweets/new_tweet.csv')

user_info = user_info.set_index('id')
tweet_info = tweet_info.set_index('id')

merge = pd.concat([user_info,
                   tweet_info],
                  axis=1,
                  join='inner')

merge.dropna(subset=['num_hashtags',
                     'num_mentions'],
             inplace=True)
merge.to_csv('csv/tweets/merged.csv', index=False)
