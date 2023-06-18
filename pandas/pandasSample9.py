import pandas as pd
import pandasql as pdql

data = pd.read_csv("/path/to/API_NY_GDP_jan142023.csv", encoding = "utf-8", on_bad_lines='skip')

sql_query = "select * from data where 'Country' = 'Japan'"

# print(pdql.sqldf(sql_query, locals()).query("'Country' == 'Japan'"))

print(pdql.sqldf(sql_query, locals()))