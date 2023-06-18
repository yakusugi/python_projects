import pandas as pd
import pandasql as pdql

data = pd.read_csv("/path/to/dataJan112023.csv")
data = data.set_index("id")

sql_query = "select * from data where gender == 'f' and age >= 30"

data2 = pd.DataFrame({"id":[2], "job":["Programmer"]})
print(data2)

sql_query = "select * from data d left join data2 d2 on d.id = d2.id"

print(pdql.sqldf(sql_query, locals()))
print(pdql.sqldf(sql_query, locals()))