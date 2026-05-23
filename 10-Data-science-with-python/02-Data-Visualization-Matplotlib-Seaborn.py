# #ex1
# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 12]
#
# plt.plot(x, y, marker='o', linestyle='-', color='b')
#
# plt.title('Simple Line Plot')
# plt.xlabel('x values')
# plt.ylabel('y values')
#
# plt.show()
#
# #ex2
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 12]
#
# plt.plot(x, y, marker='o', linestyle='-', color='b')
#
# plt.title('Simple Line Plot')
# plt.xlabel('x values')
# plt.ylabel('y values')
#
# plt.show()

#ex3
import seaborn as sns
import matplotlib.pyplot as plt

data = {'Category': ['A', 'B', 'C', 'D'], 'Values': [12, 35, 20, 40]}

import pandas as pd
df = pd.DataFrame(data)

sns.barplot(x='Category', y='Values', data=df, palette='Reds')

plt.title('Bar plot of Categories')

plt.show()