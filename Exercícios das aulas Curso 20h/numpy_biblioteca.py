import numpy as np

#criando um array
arr1 = np.array ([10,45,56,78,50])

print (arr1[0])
print(arr1)


import numpy as np
arr2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print (arr2[1,1])

#informações da matriz

print (f'Shape da matriz:{arr2.shape}')
print (f'Número de elementos da matriz:{arr2.size}')
print (f'Tipo de elementos da matriz:{arr2.dtype}')

#Operações matemáticas

arr1 = np.array([10,20,30,66,50])

print (arr1 + 10)

print (arr2 * 2)

#calculando a média

print ('Média')
print(np.mean(arr1))

#mediana = valor que está no meio quando os dados estão ordenados

print ('Mediana')
print(np.median(arr1))

#Desvio padrão

print ('Desvio padrão')
desvio_padrao = np.std(arr1)
print (desvio_padrao)

#Variância = 2 do desvio padrão

print ("Variância")
variancia = np.var(arr1)
print (variancia)

#mínimo e máximo

min = np.min(arr1)
max = np.max(arr1)

print("Mínimo",min)
print("Máximo", max)

