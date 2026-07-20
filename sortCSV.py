import pandas as pd
import re

df = pd.read_csv("cleaned_data.csv")
df2 = pd.read_csv("WVS_Wave_7_Colombia_Csv_v5.1.csv", sep=';')
df2.columns = df2.columns.str.replace('"', '').str.replace("'", "")

df2.to_csv("WVS_Wave_7_Colombia_Csv_v5.1.csv", sep=',', index=False)