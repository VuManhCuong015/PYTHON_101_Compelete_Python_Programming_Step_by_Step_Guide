#example 1
# import numpy as np
#
# arr = np.array([1,2,3,4,5])
#
# reshaped_arr = arr.reshape(1,5)
#
# multiplied_arr = arr * 2
#
# print(arr)
# print(reshaped_arr)
# print(multiplied_arr)

import pandas as pd
data = {
    'Name': ['Thomas', 'Mary', 'Karen'],
    'Age': [28, 24, 30],
    'Salary': [35000, 4500, 50000]
}

df = pd.DataFrame(data)

filtered_df = df[df['Age'] > 25]

df['Salary Increase'] = df['Salary'] * 0.1

print(filtered_df)
print(df)