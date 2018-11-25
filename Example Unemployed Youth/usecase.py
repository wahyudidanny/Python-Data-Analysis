import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')


country = pd.read_csv('E:\Github Repository\Python-Data-Analysis\Example Unemployed Youth\country_yu.csv',index_col=0)

df = country.head(5)
df = df.set_index(["Country Code"])


sd = df.reindex(columns=['2011','2012'])
print(sd)

db = sd.diff(axis=1)
db.plot(kind = 'bar')
plt.show()
             
