import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df1 = DataFrame({'key': ['a', 'd', 'c', 'a', 'b', 'd', 'c'], 'var1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'c', 'c'], 'var2': [0, 1, 2, 2]})
df = pd.merge(df1, df2, on='key', how='outer')
df.iloc[0, 2] = np.NAN
df.iloc[5, 1] = np.NAN
print('\n{0}'.format(df))
df = df.drop_duplicates()
print('\n{0}'.format(df))
print('\n{0}'.format(df.isnull()))
print('\n{0}'.format(df.dropna()))
fill_value = df[['var1', 'var2']].apply(lambda x: x.mean())
print('\n{0}'.format(df.fillna(fill_value)))
