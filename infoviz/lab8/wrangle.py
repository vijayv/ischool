import pandas as pd

df = pd.read_csv("expenditures_original.csv")
columns = df.columns.tolist()
pt = pd.melt(df, id_vars=columns[:2], value_vars=columns[2:])
pt.to_csv("expenditures_melted.csv", index=False)
