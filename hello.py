import pandas as pd
value = [100,200,300,400,500,600]
Name = [ "om", "ra", "de", "me", "ga", "Ak" ]
Indexs = [ "a", "b", "c", "d", "e", "f" ]
what = [Name, value]
df1 = pd.DataFrame( data = what, columns = Indexs)
print("df1")