import pandas as pd

df = pd.read_csv('out.csv')

df['default_profile_image'] = df['default_profile_image'].fillna(0)
df['protected'] = df['protected'].fillna(0)
df['verified'] = df['verified'].fillna(0)
df.to_csv('out2.csv')

