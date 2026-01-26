"""

EXCEÇÕES EM PYTHON
===============================

ValueError
- Valor inválido para o tipo esperado
Ex: int("abc")

TypeError
- Operação com tipos incompatíveis
Ex: 5 + "2"

NameError
- Variável ou função não definida
Ex: print(x)

IndexError
- Índice fora do alcance da lista/tupla
Ex: lista[10]

KeyError
- Chave inexistente no dicionário
Ex: dic["chave"]

ZeroDivisionError
- Divisão por zero
Ex: 10 / 0

ModuleNotFoundError
- Módulo ou pacote não encontrado
Ex: import modulo_inexistente

AttributeError
- Atributo ou método não existe no objeto
Ex: "abc".append()

FileNotFoundError
- Arquivo não encontrado
Ex: open("arquivo.txt")

KeyboardInterrupt
- Programa interrompido pelo usuário (Ctrl + C)

===============================
PADRÃO DE USO (try/except)
===============================

a=int(input("N: "))
b=int(input("N2: "))

try:
    r=a/b
except:
    print(f"PROBLEMA")
else:
    print(f"CONCLUIDO {r}")
finally:
    print("SEMPRE VOU SER EXECUTADO")


===============================

"""
'''
try: 
    a=int(input("N: "))
    b=int(input("N2: "))
    r=a/b
except (ValueError, TypeError):
    print("Erro no tipo de dado")
except ZeroDivisionError:
    print("N existe divisão por 0")
else:
    print(f'Resposta: {r}')
finally:
    print("Fechando...")
'''

#--------------------------------------------
#DESAFIOS

# 1 -> função (lerint),(leiafloat)
'''
def lerint(msg):

    while True:
        try:
            n=int(input(msg))
        except(ValueError,TypeError):
            print("Caracter Invalido")
            continue
        else:
            return n
        

def lerfloat(msg):

    while True:
        try:
            n=float(input(msg))
        except(ValueError,TypeError):
            print("Caracter Invalido")
            continue
        else:
            return n
        

def main():

    n = lerint("Inteiro: ")
    n2 = lerfloat("Real: ")

    print(f"Valor inteiro: {n} Valor Real: {n2}")

main()

'''

# 2 VER SE UM SITE ESTA ACESSIVEL 

'''

import urllib
import urllib.request

try:
    site=urllib.request.urlopen('https://pudim.com.br/')
except urllib.error.URLError:
    print("NÃO FOI POSSIVEL ABRIR")
else:
    print("SITE NO AR")
finally:
    print('SAINDO...')
'''

# 3 Sistema modularizado que permita cadastro com nome e idade
