'''
# SABENDO O LIMITE
c = 1
while c <= 10:
    print(c)
    c+=1
'''

'''
# SEM SABER O LIMITE
n=1
while n != 0:
    n = int(input("Valor para N: "))
print("FIM")
'''

'''
s = 's'
soma = 0
while s == 's':
    n = int(input("Valor: "))
    soma += n
    s = str(input("Deseja inserir mais ?")).lower()

print(f"Soma = {soma}")
'''

# LER NUMEROS CONTAR PARES E IMPARES E SEPARAR EM DUAS LISTAS
'''
n = 's'
par = 0
impar = 0
listapar = []
listaimpar = []

while n != 'n':
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        par += 1
        listapar.append(num)

    else:
        impar += 1
        listaimpar.append(num)
    n = str(input("Deseja continuar ? [s/n]")).lower()

print (f"Pares: {par} Impares: {impar}")

n = str(input("Deseja ver os numero pares e impares ?"))

if n == 's':
    print("Lista dos pares: ")
    print(listapar)
    print("Lista dos impares: ")
    print(listaimpar)
else:
    print("FIM")
'''

# EXERCICIO 1 -> DIGITAR M/F 
'''
genero = input("Digite seu gênero (M/F): ").upper()

while genero != 'M' and genero != 'F':
    print("Digite novamente da forma correta")
    genero = input("Digite seu gênero (M/F): ").upper()

if genero == 'M':
    print("Homi")
else:
    print("Louça")
'''

# EXERCICIO 2 -> FAZER JOGO DO COMPUTADOR ESCOLHER UM NUM DE 1 A 10 E EU CHUTAR
'''
import random

num = random.randint(1,10)
palpite = 0

num2=int(input("Chute de 1 a 10: "))

while num != num2:
    print("ERROU KKKKKKKKKK")
    palpite += 1
    num2 = int(input("Digite dnv: "))

print(f"ACERTOU BABACAO PRETO MACACO O NUMERO ERA {num} E VC FEZ EM {palpite} TENTATIVAS KKKKKKK")
'''

# EXERCICIO 3 -> mini calculadora
'''
num1= int(input("n: "))
num2= int(input("n: "))

operacao = 0

while operacao != 5:

    operacao = int(input(
        "Operação:\n"
        "1 - soma\n"
        "2 - multiplicar\n"
        "3 - maior\n"
        "4 - novos números\n"
        "5 - sair\n"
        "Opção: "
    ))

    if operacao == 1:
        soma = 0
        soma = num1 + num2
        print(f"soma = {soma}")
    
    elif operacao == 2:
        multi=0
        multi = num1 * num2
        print(f"multi = {multi}")

    elif operacao == 3:
        if num1 > num2: 
            print(f"{num1}")
        else:
            print(f"{num2}")

    elif operacao == 4:
        num1= int(input("n: "))
        num2= int(input("n: "))
    
    elif operacao == 5:
        print("piscando o cu lentamente")
    
print("cu negro")
'''

# EXERCICIO 4 -> ler um numero e mostrar seu fatorial
'''
num = int(input("Num: "))
fat = 1
while num != 0:
    fat *= num
    num -= 1

print(f"{fat}")
'''

# EXERCICIO 4 (FOR)
'''
num = int(input("Num: "))

fat = 1

for c in range (num):
    fat *= num
    num -= 1

print(f"{fat}")
'''

# EXERCICIO 5 -> ler um numero e a razao para fazer uma PA mostrando os 10 primeiros termos
'''
num = int(input("Primeiro termo: "))
raz = int(input("Razão: "))

contador = 0
termo = num

while contador < 10:
    print(termo)
    termo += raz
    contador += 1
'''

# EXERCICIO 6 -> mostrar mais termos para o usuario 
'''
num = int(input("Primeiro termo: "))
raz = int(input("Razão: "))

contador = 0
termo = num

while contador < 10:
    print(termo)
    termo += raz
    contador += 1

ordem = int(input("Quer quantos a mais ?: "))
contador = 0

while contador < ordem:
    print(termo)
    termo+=raz
    contador+=1
'''

# EXERCICIO 7 -> ler infinitos numeros ate ser digitado 999
'''
num = int(input("NUM: "))
soma = 0
qnt = 1
while num != 999:
    num = int(input("Novamente: "))
    soma += num
    qnt += 1
print(f"{soma}  {qnt}")
'''

# EXERCICIO 8 -> ler varios numeros e mostrar a media, o maior e o menor

soma = 0
quantidade = 0
maior = None
menor = None
resposta = 's'

while resposta == 's':
    num = int(input("Número: "))

    soma += num
    quantidade += 1

    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

    resposta = input("Deseja continuar? [s/n] ").lower()

media = soma / quantidade

print(f"Média: {media}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")







    







    

