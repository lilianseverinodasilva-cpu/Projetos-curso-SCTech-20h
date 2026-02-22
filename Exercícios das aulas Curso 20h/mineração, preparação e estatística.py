import pandas as pd

""" # Criando uma serie
serie = pd.Series([10,20,30,40,50])

print(serie) """

data = {
    'Nome': ['Alice','Bob','Charlie','David'],
    'Idade': [25,30,35,40],
    'Cidade':['São Paulo','Rio de Janeiro', 'Salvador', 'Itajaí']

}

df = pd.DataFrame(data)

print(df)

print(df['Nome'])

print (df.iloc[0])

print(df.loc[0,'Nome'])