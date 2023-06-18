import pandas as pd
import pandasql as pdql

data = pd.read_csv('./nasdaq100/small/nasdaq100_padding.csv')
data = data.set_index("id")

sql_query = "select * from data"

print(pdql.sqldf(sql_query, locals()))