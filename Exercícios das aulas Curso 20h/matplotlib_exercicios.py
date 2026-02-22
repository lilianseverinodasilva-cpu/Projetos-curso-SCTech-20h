import matplotlib.pyplot as plt

#gráfico de linhas

""" plt.plot([1,2,5,6],[7,89,4,5])

plt.show() """

#Dados

""" x = ['Maçãs', 'Morangos', 'Uvas']
y = [5,18,9]

plt.bar(x,y, color ='pink')

plt.xlabel('Frutas')
plt.ylabel('Quantidade')
plt.title('Quantidade de frutas')

plt.show() """

#gráfico de pontos

""" x = [3,5,8,3,65,24,60]
y = [45,3,7,98,23,11,34]
plt.xlabel('Nº pessoas')
plt.ylabel('Compras feitas')

plt.scatter(x,y,label='Pontos',color='b',marker='.', s=100)
plt.legend()
plt.show() """

#criando outro gráfico

import seaborn as sns

titanic = sns.load_dataset('titanic')
df_por_sexo = titanic.groupby('sex')['survived'].sum().reset_index()

plt.figure(figsize=(8,6))

sns.barplot(df_por_sexo,x='sex',y='survived')

plt.show()

