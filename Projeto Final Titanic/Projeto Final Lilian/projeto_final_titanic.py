import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#EDA = Exploratory Data Analysis



#EDA 1 - Importar o conjunto de dados

df = pd.read_csv('titanic_dataset.csv')

#Aqui pedi ajuda da IA
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)



#EDA 2 - Compreender o quadro geral

print(df.head())
print(df.info())
print(df.describe())

#Datatypes

print(df.dtypes)

#Filtros

print(df[df['Age'] <=10].head())



#EDA 3 - Preparação dos dados

duplicateRows = df[df.duplicated()]
##No arquivo dispolinilizado no Drive parece que já não tinha nenhum dado duplicado, uma vez que ao fazer o código abaixo, o valor foi 0
print(len(duplicateRows))

##Continuando a limpeza de dados, apesar de não haver duplicados
print(len(duplicateRows))
df.drop_duplicates(keep='last',inplace=True)
print(len(duplicateRows))

#Removendo valores nulos

#Comentei o código abaixo para ele manter os dados da coluna "Cabin" como 0 e não para apagar dados
""" df.dropna(subset=['Cabin'],inplace=True) """

#Substituir nulos
""" #Tive que comentar este código porque ele substituiu todos os valores Nan por 0 para além da coluna "Cabin", o que modificou os dados
df.replace(np.nan,0,inplace=True)
print(df.head()) """

#Renomear colunas
df = df.rename(columns={'Sex':'Gender'})
print(df.head())

#Filtragem/Sort

#Daqui em diante eu só quero ver as 6 primeiras colunas, e tive que pedir ajuda à IA
df_to_understand = df.loc[:, ['PassengerId','Survived','Pclass','Gender','Age','Cabin']]

sorted_df = df_to_understand.sort_values(by='Gender',ascending=True)
print(sorted_df.head(10))

sorted_df = df_to_understand.sort_values(by='Pclass',ascending=True)
print(sorted_df.head(10))

#Agrupamento

#tive problemas com o código deixando apenas um item, como "Age", então tive que pedir ajuda à IA e ela aconselhou utilizar dois grupos para análise, porque o Python não entendia os valores de string nas colunas.
print(df.groupby('Gender')['Survived'].mean())
print(df_to_understand.head())

#Outliers
sns.boxplot(x=df['Age'])
plt.show()




#EDA 4 - Compreensão das variáveis

#contagem

survived_counts = df_to_understand['Survived'].value_counts()
print(survived_counts)

gender_counts = df_to_understand['Gender'].value_counts()
print(gender_counts)





#EDA 5 - Estudo das realções entre variáveis


# Análise de sobreviventes
plt.figure(figsize=(6,4))
plt.bar(survived_counts.index,survived_counts,color='black')
plt.title('Contagem de sobreviventes')
plt.xlabel('Sobreviveu? 0=Não / 1=Sim')
plt.ylabel('Número de sobreviventes')

plt.show()


#Sobrevivente x sexo
df_por_sexo = df_to_understand.groupby('Gender')['Survived'].sum().reset_index()
plt.figure(figsize=(8,6))
sns.barplot(df_por_sexo,x='Gender',y='Survived')
plt.show()


#Análise de sobreviventes x idade (aqui usei um pouco de IA)

plt.figure(figsize=(10, 6))
sns.stripplot(x='Survived', y='Age', data=df_to_understand, hue='Survived', palette='pink', size=3, jitter=True)
plt.title('Distribuição de Sobrevivência por Idade')
plt.xlabel('Sobreviveu? (0 = Não, 1 = Sim)')
plt.ylabel('Idade')
plt.show()





#EDA 6 - Debate sobre resultados

"""
ANÁLISE DOS RESULTADOS:
- O último gráfico deixa claro que mais mulheres sobreviveram que homens.
- Faz sentido, pois mulheres e crianças tiveram prioridade nos botes.
- No terceiro gráfico, nota-se maior concentração de não sobreviventes de idade avançada"""