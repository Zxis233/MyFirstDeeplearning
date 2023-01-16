import pandas as pd


""" df_all = []
for i in range(1, 6):
    df_all.append(pd.read_csv(f"csv/tweets/{i}.csv", encoding='utf-8'))
# print(df_all[0])

tweets_csv = pd.concat(df_all, ignore_index=True)

records = [
    (
        getattr(row, 'user_id'),

        # NETWORK ATTRIBUTE
        getattr(row, 'num_hashtags'),
        getattr(row, 'num_mentions'),

    )
    for row in tweets_csv.itertuples()
]

out = pd.DataFrame.from_records(
    records,
    columns=[
        'user_id',
        'num_hashtags',
        'num_mentions',
    ]
)
out.to_csv('csv/tweets/out.csv', index=False) """

new_tweets = pd.read_csv('csv/tweets/out.csv', encoding='utf-8')

tweet_dict = {}

for row in new_tweets.itertuples():
    user_id = str(getattr(row, 'user_id'))
    hashtags = int(getattr(row, 'num_hashtags'))
    mentions = int(getattr(row, 'num_mentions'))
    # print(hashtags, mentions)

    if user_id not in tweet_dict:
        tweet_dict[f"{user_id}"] = [hashtags, mentions]

    else:
        tweet_dict[f"{user_id}"][0] += hashtags
        tweet_dict[f"{user_id}"][1] += mentions

new_tweet_csv = pd.DataFrame.from_dict(tweet_dict)
new_tweet_csv = new_tweet_csv.T.reset_index(drop=False)
new_tweet_csv.columns = ['id', 'num_hashtags', 'num_mentions']
new_tweet_csv.to_csv('csv/tweets/new_tweet.csv', index=False)

# new_tweet_csv.to_csv('csv/tweets/new.')
