import pandas as pd

df1 = pd.DataFrame({"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                    index = [2001,2002,2003,2004])

df2 = pd.DataFrame({"Lowe_Tier_HPI":[2,1,2,3],"Unemployement":[1,3,4,7]},
                    index = [2001,2003,2004,2004])

joined = df1.join(df2)

print(joined)
