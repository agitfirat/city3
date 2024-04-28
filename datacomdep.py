import pandas as pd 

df=pd.read_csv('data_com-2.csv', sep=';', encoding="ISO-8859-1")

for i in range(len(df)): 
    df.loc[i,'code_dep'] = df.loc[i,'com_code'][:2]

df.to_csv("data_com-2.csv")