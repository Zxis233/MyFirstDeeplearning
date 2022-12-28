"""
   @Author: Esing
   @Date: 22:29
   @FilePath: 
   @Editor: PyCharm
"""

from datetime import datetime
import json
import pandas as pd
import re


def get_time_to_now(user_time: str):
    GMT_FORMAT = "%a %b %d %H:%M:%S +0000 %Y"
    real_time = datetime.strptime(user_time, GMT_FORMAT)
    t1 = real_time.date()
    now_time = datetime.now()
    t2 = now_time.date()
    days = (t2 - t1).days
    return int(days)


def get_url(url: str) -> bool:
    if url is None or url == ' ':
        return False
    else:
        return True


# name = "botometer-feedback-2019_tweets"
name = "gilani-2017_tweets"

origin_data = json.load(open(name + ".json"))

records = [
    (
        i['user']['id'],
        i['user']['followers_count'],
        i['user']['friends_count'],
        i['user']['statuses_count'],
        i['user']['listed_count'],

        get_time_to_now(i['created_at']),
        get_url(i['user']['profile_image_url_https']),
        i['user']['protected'],
        i['user']['verified'],
        len(i['user']['name']),
        len(i['user']['screen_name'])
    )
    for i in origin_data
]

out = pd.DataFrame.from_records(
    records,
    columns=[
        'id',
        'followers_count',
        'following_count',
        'tweet_count',
        'listed_count',
        'time_to_now',
        'has_profile_photo',
        'protected',
        'verified',
        'nickname_length',
        'screenname_length'
    ]

)

out = out.drop_duplicates(subset=['id'])
out.to_csv(name + '.csv', index=False)
