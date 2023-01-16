import pandas as pd
from datetime import datetime

from entropy import calEntropy
from true_or_false import judge_tof


# from check import get_time_to_now, get_url

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


# STAGE ONE:
#
# 剔除无用行，并且将数据集所对应的用户更改为是否为机器人(0/1)


df_all = []
for i in range(1, 6):
    df_all.append(pd.read_csv(f"csv/{i}.csv"))
# print(df_all[0])

all_csv = pd.concat(df_all, ignore_index=True)

all_csv = all_csv.drop(
    axis=1, columns=
    [
        "id",
        "time_zone",
        "profile_image_url",
        "profile_background_image_url_https",
        "profile_text_color",
        "profile_sidebar_border_color",
        "profile_sidebar_fill_color",
        "profile_background_color",
        "profile_link_color",
        "utc_offset",
        "profile_background_image_url",
        "lang",
        # "description",
        "url",
        "profile_image_url_https",
        "profile_banner_url",
        "geo_enabled"

    ]
)

all_csv.rename(columns={'dataset': 'is_human'}, inplace=True)

all_csv.loc[all_csv['is_human'] == 'TWT', 'is_human'] = '0'
all_csv.loc[all_csv['is_human'] == 'E13', 'is_human'] = '1'
all_csv.loc[all_csv['is_human'] == 'INT', 'is_human'] = '0'
all_csv.loc[all_csv['is_human'] == 'FSF', 'is_human'] = '0'
all_csv.loc[all_csv['is_human'] == 'TFP', 'is_human'] = '1'
# all_csv.loc[all_csv['verified'] != , 'verified'] = '1'

# all_csv = all_csv.dropna(axis=0, subset=['is_human'], how='any')
all_csv = all_csv.dropna(axis=0, subset=['screen_name'], how='any')
# all_csv = all_csv.fillna({'verified': 0})
all_csv.to_csv('all.csv', index=False)

# STAGE TWO:
#
# 读取新生成的CSV文件，进行预处理

train_csv = pd.read_csv('all.csv')
'''
records = [
    (
        getattr(row, 'followers_count'),
        getattr(row, 'friends_count'),
        getattr(row, 'statuses_count'),
        getattr(row, 'listed_count'),
        get_time_to_now(getattr(row, 'created_at')),
        getattr(row, 'default_profile_image'),
        getattr(row, 'protected'),
        getattr(row, 'verified'),
        len(str(getattr(row, 'description'))),
        len(getattr(row, 'name')),
        len(getattr(row, 'screen_name')),
        getattr(row, 'is_human'),
    )
    for row in all_csv.itertuples()
]

out = pd.DataFrame.from_records(
    records,
    columns=[
        'followers_count',
        'following_count',
        'tweet_count',
        'listed_count',
        'time_to_now',
        'default_profile_image',
        'protected',
        'verified',
        'description',
        'nickname_length',
        'screenname_length',
        'is_human'
    ]

)

out.to_csv('out.csv', index=False)
'''

# print(all_csv['location'].isnull())

# for i in all_csv[:5].itertuples():
#     print(getattr(i, 'default_profile'))
#     print(str(getattr(i, 'default_profile')) == 'nan')

records = [
    (
        # USER ATTRIBUTE
        len(getattr(row, 'screen_name')),
        1 if str(getattr(row, 'default_profile')) != 'nan' else 0,

        calEntropy(str(getattr(row, 'screen_name'))),

        1 if str(getattr(row, 'location')) == 'nan' else 0,

        getattr(row, 'statuses_count'),

        # NETWORK ATTRIBUTE
        getattr(row, 'friends_count'),
        getattr(row, 'followers_count'),

        # CONTENT
        getattr(row, 'is_human'),

        # TIMING
        get_time_to_now(getattr(row, 'created_at')),
        float(getattr(row, 'statuses_count')) / float(get_time_to_now(getattr(row, 'created_at'))),
    )
    for row in all_csv.itertuples()
]

out = pd.DataFrame.from_records(
    records,
    columns=[
        'screenname_length',
        'default_profile',
        'screenname_entropy',

        'has_location',
        'total_tweets',

        'of_friends',
        'of_followers',

        'is_human',

        'account_age',
        'avg_tweets_per_day'
    ]
)

out.to_csv('out.csv', index=False)
