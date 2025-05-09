import pandas as pd

df = pd.read_csv('melate.csv')
#agrupado1 = df.groupby('R2').describe().xs('count', level=1, axis=1)['R1']
#agrupado2 = df.groupby('R2').describe().loc[:, (slice(None), 'count')]
#agrupado3 = df.groupby('R3').describe().loc[:, (slice(None), 'count')]
#agrupado4 = df.groupby('R4').describe().loc[:, (slice(None), 'count')]
#agrupado5 = df.groupby('R5').describe().loc[:, (slice(None), 'count')]
#agrupado6 = df.groupby('R6').describe().loc[:, (slice(None), 'count')]

#sum=df[df['R1']==7]['BOLSA'].sum()
#data_shape = df.shape
print(df.drop_duplicates().columns)

states  = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camellia', 'Forget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-spotted skimmer dragonfly', 'Two-tailed swallowtail', 'European honey bee']
index   = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)

print(df)
print()
print(df.iloc[3, 2]) 