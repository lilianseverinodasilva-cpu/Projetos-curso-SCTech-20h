""" frutas = ["Maçã", "Banana", "Laranja", "Abacaxi", "Uva"]
print(frutas)


for fruta in frutas:
    print(fruta) """


""" num = 1
while num <= 5:
    print(num)
    num += 1.5 """


#DESAFIO


""" 
frutas = ["Maçã", "Banana", "Laranja", "Abacaxi", "Uva"]


frutas = []
frutas.append("Melancia")
frutas.append("Maçã")
frutas.append("Abacaxi")
print(frutas)

frutas.pop()
print(frutas)
frutas.append("Kiwi")
print(frutas)

from collections import deque
fila = deque()
frutas.append("Morango")
frutas.append("Acerola")
frutas.append("Cranberry")
print(frutas)

frutas.pop(0)
print(frutas) 
frutas.append("Uva")


for fruta in frutas:
    print(fruta)



for fruta in frutas:
    if fruta == "Maçã" or fruta == "Laranja":
        print("Encontrei a maçã e a Laranja!")
        print(fruta) """


""" hora = 1
humor = 'blabla'

if humor == 'sono' and hora < 10:
    print("Café")  
elif humor == 'sedento' or hora < 2:
    print("Limonada")
else:
    print("Água") """


""" planetas = ["Mercurio", "Marte", "Terra", "Jupíter", "Saturno", "Netuno", "Venus", "Urano"]

for planeta in planetas:
    print('Planeta:', planeta)

for i in range(5):
    print('Planeta', i,':', planeta)

i=0
while i<10:
    print(i,end='')
    i+=1
    # i += 1 / i = i + i """


#DESAFIO


início = 1
fim = 10

for num in range (início, fim+1):
    if num % 2 == 0:
        print (num)

