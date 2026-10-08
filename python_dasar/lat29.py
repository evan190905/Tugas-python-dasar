import pandas as pd

df = pd.read_csv('nilai.csv')
print(df.groupby('kelas').agg({'nilai': ['count', 'mean']}))
print(df[df['nilai'] >= 75]["nilai"].tolist())
print(df.sort_values("nilai").tail(1))