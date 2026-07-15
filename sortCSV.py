import pandas as pd
import re

df = pd.read_csv("cleaned_data.csv")
df2 = pd.read_csv("WV6_Data_Colombia_Csv_v20221117.csv", sep=',')

df.columns = df.columns.str.lower()

df2.columns = df2.columns.str.replace("'", "").str.replace('"', "")

race_responses = df["race"]

q48_responses= df2["V48"]

q48_responses.to_csv("lookup.txt", index=False)

df2.to_csv("WV6_Data_Colombia_Csv_v20221117.csv", index=False)


