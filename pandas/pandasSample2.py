import pandas as pd
import pandas as pdql

data = pd.read_csv("/path/to/dataJan112023.csv")
data = data.set_index("id")

print(data.query("age >= 30"))