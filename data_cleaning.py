import pandas as pd 

df = pd.read_csv("final.csv")
print(df.shape)

del df["Star_names"]
del df["Mass.1"]
del df["Radius.1"]
del df["Distance.1"]

print(df.shape)
df.to_csv('main.csv') 