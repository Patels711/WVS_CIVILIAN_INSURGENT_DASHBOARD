import pandas as pd
import re

df = pd.read_csv("cleaned_data.csv")
df2 = pd.read_csv("WVS_Wave_7_Colombia_Csv_v5.1.csv", sep=';')

df.columns = df.columns.str.lower()

df2.columns = df2.columns.str.replace("", "").str.replace('',"")
df2.columns = df2.columns.str.replace(";", ",")

race_responses = df["race"]

q48_responses= df2["Q33_3"]

q48_responses.to_csv("lookup.txt", index=False)

df2.to_csv("WVS_Wave_7_Colombia_Csv_v5.1.csv", index=False)


