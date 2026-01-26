# LISTAS

#1 -> ler varios num, armazenar em uma lista, mostrar: qnt, ordem crescente, se o num 5 foi digitado ou n
'''
lista = []
qnt = 0
while True:
    num = int(input("Num: "))
    qnt += 1
    lista.append(num)
    resp = input("Deseja continuar ?").lower()

    if resp != 's':
        break
    else:
        print("Armazenado ...")

    if num == 5:
        print("Num 5 digitado")

lista.sort()
print(f"Quantidade de elementos: {qnt}")
print(lista)
'''

#2 -> ler valores, nao permitir valores repetidos e mostrar em ordem
'''
from random import randint
from time import sleep

lista = []

while True:
    num = randint(0,100)
    

    if num in lista:
        print("Ja em uso este valor")
    else:
        
        lista.append(num)

    resp = input("Deseja continuar ? [s/n]").lower()

    if resp != 's':
        break
        sleep(0.5)

    print(f"Armazenado o valor {num}")


resp2 = int(input("Digite '1' para crescente e '2' para decrescente "))

if resp2 == 1:
    lista.sort()
    print(lista)
elif resp2 == 2:
    lista.sort(reverse=True)
    print(lista)
else:
    print("BABACAO")
'''

#3 -> NOME,IDADE,SEXO, mostrar tudo se e de maior e se e mulher
'''
from time import sleep
from datetime import datetime

registro = {}

registro['NOME'] = input("Digite seu nome: ")
nascimento = int(input("Digite seu nascimento: "))
registro['SEXO'] = input("Digite seu sexo: [m/f]").lower()
registro['IDADE'] = datetime.now().year - nascimento

resp = int(input("1-> mostrar meus dados, 2-> se posso dirigir, 3-> se posso lava louça: "))

if resp == 1:
    print(f"Imprimindo dados de {registro['NOME']}")
    sleep(0.5)
    print(registro)

elif resp == 2:
    if registro['IDADE'] >= 18:
        print("Liberado")
    else:
        print("N pode")

elif resp == 3:
    if registro['SEXO'] == 'f':
        print("Liberada")
    else:
        print("vai para guera kkkkkk ")
'''

#4 -> ler nome,sexo de varias pesssoas, guardar em uma lista todas as pessaos, A) quantas pessoas foram cadastradas, B) media de idade, C) uma lista com as mulheres, D) uma lista com todas as pessaos acima da media
from time import sleep
pessoa = {} #-> dic
galera = [] #-> list

qnt = soma = 0

while True:
    pessoa.clear()
    pessoa['NOME'] = input("Digite seu nome: ").upper()
    pessoa['SEXO'] = input("Sexo: [m/f]")
    pessoa['IDADE'] = int(input("Idade: "))

    qnt += 1
    soma += pessoa['IDADE']
    galera.append(pessoa.copy())

    resp = input("Deseja continuar ? [s/n]").lower()
    if resp != 's':
        break
    print("Registrando...")
    sleep(0.5)

media = soma / qnt


print("-=" *30)
print(f"Total de Pessoas: {qnt}")
print(f"Media da idade: {media:.1f}")

print("\n LISTAGEM DAS MULHERES:")
for p in galera:                #O 'P' E CADA POSIÇÃO DA LISTA, ASSUMINDO A POSIÇÃO DE UM DOS DICIONARIOS POR VE
    if p['SEXO'] == 'f':
        print(p['NOME'])
    
print("\n LISTAGEM DOS ACIMA DA IDADE: ")
for p in galera:
    if p['IDADE'] >= media:  
        print(p['NOME'])








    
