import pandas as pd
import pandasql as pdql

data = pd.read_csv("/path/to/dataJan112023.csv")
data = data.set_index("id")

sql_query = "select * from data where gender == 'f' and age >= 30"

print(pdql.sqldf(sql_query, locals()))