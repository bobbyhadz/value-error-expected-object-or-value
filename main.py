# ValueError: Expected object or value with `pd.read_json()`

import pandas as pd

data = pd.read_json('data.json')

#     name  experience  salary
# 0  Alice          10   175.1
# 1  Bobby          13   180.2
# 2   Carl          15   190.3
print(data)
