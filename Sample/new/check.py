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


# origin_data = json.load(open("test.json"))
origin_data = json.load(open("node.json"))

records = [
    (
        i['public_metrics']['followers_count'],
        i['public_metrics']['following_count'],
        i['public_metrics']['tweet_count'],
        i['public_metrics']['listed_count'],
        get_time_to_now(i['created_at']),
        get_url(i['profile_image_url']),
        i['protected'],
        i['verified'],
        len(i['name']),
        len(i['username'])
    )
    for i in origin_data
]

out = pd.DataFrame.from_records(
    records,
    columns=[
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

# out.to_csv('test.csv')
out.to_csv('out.csv')
