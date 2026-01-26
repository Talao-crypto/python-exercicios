# for i in range(1,10):


# MATRIZ 
'''
for i in range (5):
    for j in range (3):
        print(f"i={i}, j={j}")
'''

# FOR I IN RANGE (1, 6, -1) -> CONTAGEM REGRESSIVA -1  (O PRIMEIRO DEVE SER MAIOR Q O SEGUNDO)
'''
for i in range (6, 0, -1):
    print(f"{i}")
print('fim')
'''

# FUNCIONALIDADE DE IR PULANDO FOR I IN RANGE (0,7,2) -> PULA DE 2 EM 2 NESTE CASO 
'''
i = int(input("inicio: "))
f = int(input("fim: "))
p = int(input("passo: "))
for i in range(i,f,p):
    print(f"i={i}")

'''


# EXERCICIO 1 -> CONTAGEM REGRESSIVA DE 1 A 10 COM PAUASA DE 1 SEGUNDO ENTRE ELES E NO FINAL DAR UM BOOM
import time
'''
for i in range (10,0,-1):
    print(i)
    time.sleep(1)
print("CU PRETO")
'''


#EXERCICIO 2 -> MOSTRAR TODOS OS PARES DE 1 A 50

'''
for i in range(1,51):
    if i % 2 == 0:
        print(i)
'''

#EXERCICIO 3 -> MOSTRAR A SOMA DE TODOS OS NUMEROS IMPARES E MULTIPLOS DE 3 DE 1 A 500
'''
soma = 0
for i in range(1,501):
    if i % 2 != 0:
        if i % 3 == 0:
            soma += i
    
print(f"soma = {soma}")
'''

# EXERCICIO 4 -> LER 6 NUMEROS E MOSTRAR A SOMA DOS PARES 
import random 
'''
soma = 0
print ("Valores somados: ")
for i in range (1,7):
    n = random.randint(0,100)

    if n % 2 == 0:
        print(f"{n} ")
        soma += n

print(f'soma={soma}')
'''

#exercicio 5 -> LER O PRIMEIRO TERMO E A RAZAO DA PA, E MOSTRAR OS 10 PRIMEIROS TERMOS DESTA PA
'''
i = int(input("inicio: "))
r = int(input("razão: "))

for c in range (i,i+10, r):
    print(c)
'''

# EXERCICIO 6 -> LER INTEIRO E VER SE ELE E PRIMO 
'''
from colorama import Fore, Back, Style, init
init()

num = int(input("Digite um numero: "))
qnt=0

for i in range (1,num+1):
    if num % i == 0:
        qnt += 1
        print(Fore.RED + str(i) +Style.RESET_ALL)
    else:
        print(i)

if qnt == 2:
    print("Primo")

else:
    print("N primo")
'''




# EXERCICIO 7 -> ler uma frase e ver se e um palindromo
'''
palavra=input("Digite a palavra ")

palavra = palavra.replace(" ","").lower()
invertida = ""

for i in range (len(palavra) - 1, -1, -1):
    invertida += palavra[i]

if (palavra == invertida):
    print('1')
else:
    print("0")
'''

# EXERCICIO 8 -> LER 7 DATAS DE NASCIMENTO, MOSTRAR QUANTAS SAO DE MAIORES E QUANTAS DE MENOR
'''
maior = 0
menor = 0

for i in range(7):
    idade = int(input("nascimento: "))
    if 2025 - idade > 18:
        maior += 1
    else:
        menor += 1

print(f"maiores: {maior}, menores: {menor}")
'''


# EXERCICIO 9 -> LER O PESO DE 5 PESSOAS E MOSTRAR O MAIOR E O MENOR PESO LIDO
'''
maior = 0
menor = 10000


for i in range (5):
    peso = int(input("Peso: "))

    if peso > maior:
        maior = peso
    
    if peso < menor:
        menor = peso


print(f"maior {maior}, menor {menor}")
'''

# EXERCICIO 10 -> LER NOME,IDADE, SEXO DE 4 PESSOAS E MOSTRAR -> MEDIA DE IDADE -> HOMEM MAIS VELHO E QUANTAS MULHERES TEM MENOS DE 20
'''
media_idade = 0
nome_homem_velho = ''
idade_homem_velho = 0
qnt_mulher = 0

for i in range(4):
    nome = input("Seu nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (m/f): ").lower()

    media_idade += idade

    if sexo == 'm':
        if idade > idade_homem_velho:
            idade_homem_velho = idade
            nome_homem_velho = nome

    if sexo == 'f' and idade < 20:
        qnt_mulher += 1

media_idade /= 4

print(f"Média de idade do grupo: {media_idade:.2f}")
print(f"Homem mais velho: {nome_homem_velho} ({idade_homem_velho} anos)")
print(f"Mulheres com menos de 20 anos: {qnt_mulher}")
'''


# EXERCICIO EXTRA -> PEDIR NUM E FAZER CONTAGEM ATE ESSE NUM E A SOMA DE TUDO
'''
num = int(input("num: "))
soma = 0

for i in range(0,num+1):
    soma += i

print(f"soma = {soma}")
'''

# EXERCICIO EXTRA -> Tabuada
'''
num = int(input("num: "))

for i in range(0,11):
    multi=0
    multi = num * i
    print(f"{num} x {i} = {multi}")
'''

# EXERCICIO EXTRA -> MATRIZ E O VALOR DA SOMA DELA
'''
soma = 0
for i in range (3):
    for j in range (3):
        num = int(input(f"Valor de {i} {j}: "))
        soma += num

print(f"soma = {soma}")
'''

# EXERCICIO EXTRA -> SOMAR DIAGONAL PRINCIPAL (I,I)
'''
import random
soma = 0

for i in range (3):
    for j in range (3):
        num = random.randint(0,15)
        if i==j:
            soma += num

print(f"soma = {soma}")
'''

# EXERCICIO EXTRA -> CONTAR VALORES PARES E VALORES IMPARES E VER QUAL TEM MAIS
'''
import random

par = 0
impar = 0

for i in range (4):
    for j in range (4):
        num = random.randint(0,200)
        if num % 2 == 0:
            par += 1
        else:
            impar += 1

resultado = 0
if par > impar:
    resultado = par - impar
    print(f"Par é maior pois temos {resultado} pares a mais que impares")

elif impar > par:
    resultado = impar - par
    print(f"Impar é maior pois temos {resultado} impares a mais que par")

else:
    print(f"MESMA QUANTIDADE")
'''









