import pandas as pd
# from pandas import DataFrame

dataframes = []

data = [{'id': 1, 'title' : 'визитка'}]

df = pd.DataFrame(data)
dataframes.append(df)
df2 = pd.DataFrame(data)
dataframes.append(df2)
# df.to_excel('result.xlsx', index=None)


print(dataframes)