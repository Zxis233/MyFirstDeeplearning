import pandas as pd

name = "botometer-feedback-2019"
# name = "gilani-2017"

names = ['id', 'type']

chunks = pd.read_csv(name + '.tsv', sep='\t', on_bad_lines='skip', header=None, names=names, iterator=True)
chunk = chunks.get_chunk()
# print(chunk)
chunk = chunk.drop_duplicates(subset=['id'])
chunk.to_csv(name + '_detect.csv', index=False)
