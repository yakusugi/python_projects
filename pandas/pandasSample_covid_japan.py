import pandas as pd
import pandasql as pdql

data = pd.read_csv("/shares/smb/seagate_hdd_5tb/Python/pandas/deaths_cumulative_daily_original.csv")
# data = data.set_index("id")

sql_query = "select * from data where Date == Datetime('5/28/2021 00:00:00')"

# print(pdql.sqldf('''SELECT
#   *
# , date('%d', '5/28/2021') AS Day 

#  FROM data
#  '''), locals())


# sql_query = "select Date(5/28/2021)"

print(pdql.sqldf(sql_query, globals()))