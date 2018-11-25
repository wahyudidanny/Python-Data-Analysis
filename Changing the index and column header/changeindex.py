import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")


#change the column header
df = pd.DataFrame({"Day":[1,2,3,4],"Visitors":[200,100,230,300],"Bounce Rate":[20,45,60,10]})
df = df.rename(columns={"Visitors":"Users"})
print(df)



# change the index header
#df.set_index("Day",inplace=True)# change index 
#print(df)

#df.plot()
#plt.show()
