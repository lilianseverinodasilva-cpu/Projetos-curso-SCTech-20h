""" def somar (A,B):
    return A+B

resultado = somar (2,3)
print (resultado) """


""" #FUNÇÃO PURA

def pure_increments(elements, index):
    new_elements = elements.copy()
    new_elements [index] += 1
    return new_elements

lista = [1,2,3,4,5,6,7,8,9]

print (pure_increments (lista,1) )

print (lista) """


# erros

def dividir (a,b):
    r = 0
    try: 
        r = a/b
        return print(r)
    except ZeroDivisionError:
        print ('Erro: Divisão por zero')
    except:
        print ('Erro inesperado. Desculpe')
    finally:
        print ('Função executada')

print(dividir (8,'a'))
