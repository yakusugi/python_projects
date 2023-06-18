import pandas as pd
import pandasql as pdql

data = pd.read_csv("/path/to/API_NY_GDP_MKTP.csv", on_bad_lines='skip')
# data = data.set_index("id")

sql_query = "select * from data where 'Country' == 'Japan'"

print(pdql.sqldf(sql_query, locals()))