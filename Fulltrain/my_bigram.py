import json

import pandas as pd
from tqdm import tqdm

dataset = 'cresci-2015'
pbar = tqdm(ncols=0)
pbar.set_description(dataset)

path = 'all.csv'

ch_list = [chr(i) for i in range(65, 91)] + \
          [chr(i) for i in range(97, 123)] + \
          [chr(i) for i in range(48, 58)] + ['_']

bi_gram_count = {}

for x in ch_list:
    for y in ch_list:
        tmp = x + y
        bi_gram_count[tmp] = 0

data = pd.read_csv('all.csv')

for row in data.itertuples():
    pbar.update()
    username = getattr(row, 'screen_name')
    if username is None:
        continue
    username = username.strip()
    for index in range(len(username) - 1):
        bi_gram = username[index] + username[index + 1]
        bi_gram_count[bi_gram] += 1

bi_gram_sum = 0
for value in bi_gram_count.values():
    bi_gram_sum += value
for item in bi_gram_count:
    bi_gram_count[item] /= bi_gram_sum
json.dump(bi_gram_count, open(f'{dataset}_bi_gram_likelihood.json', 'w'))
