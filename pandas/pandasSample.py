import pandas as pd
import pandas as pdql

data = pd.read_csv("/shares/smb/seagate_hdd_5tb/Python/pandas/dataJan112023.csv")
data = data.set_index("id")

print(data)