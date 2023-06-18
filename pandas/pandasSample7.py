import pandas as pd
import pandasql as pdql

data = pd.read_csv("/path/to/dataJan112023.csv")
# data = data.set_index("id")

sql_query = "select * from data where country == 'Mexico' and age_cat == '18-24' and sex == 'Women'"

print(pdql.sqldf(sql_query, locals()))