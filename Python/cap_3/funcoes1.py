# definir uma função -> def (nome)():
# chamar uma função -> (nome)()

'''
def linha():
    print("*-=" *30)

def nome(texto):
    print(texto *30)

def main():
    linha()
    nome("Tales")
    linha()

main()
'''
#--------------------------------------------------------------------

'''
def linha():
    print("-=" *15)

def titulo(txt):
    print(txt)
    linha()

def main():
    titulo('Ola')
    titulo('Mundo')

main()
'''
#--------------------------------------------------------------------

'''
def soma(x,y):
    s = x + y
    return s

def main():
    n1 = int(input("N: "))
    n2 = int(input("N2: "))

    resul = soma(n1,n2)
    print(f"A soma de {n1} e {n2}")
    print(f"Resultado: {resul}")

main()
'''

#--------------------------------------------------------------------

# EMPACOTAMENTO
'''
def contador(*num):
    for i in num:
        print(i, end=" ")
    print("FIM")

    tam = len(num)
    print(f'Recebi os valores de {num} e tem {tam} valores')

contador(2, 3, 4, 5, 1)
contador(1, 2, 3, 4, 5)
contador(1000)
'''
#--------------------------------------------------------------------

#LISTA EM FUNÇÕES
'''
def dobra(list):
    
    for i in range(len(list)):
        list[i] *= 2



valores = [1,2,3,4,5,6]
dobra(valores)
print(valores)
'''
#--------------------------------------------------------------------

'''
def soma(*num):
    s = 0
    for i in num:
        s += i
    
    print(f"Somando os {num} temos {s}")

def main():

    soma(2,4,5,6,7)
    soma(1,2)
    soma(1,6,9,2)

main()
'''
