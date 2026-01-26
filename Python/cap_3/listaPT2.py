#lista dentro de lista

'''
dados = []
dados.append("Pedro")
dados.append(25)
pessoas = []

pessoas.append(dados[:])  -> no elemento "0" de pessaos vai ter toda a estrutura do dados
print(pessoas[0][0]) -> indice "0" de pessoas e primeiro indice dentro do indice
print(pessoas[1]) -> vai printar a lista inteira do indice '1'
'''


                                                            #PRATICA
#---------------------------------------------------------------------
'''
teste = list()
teste.append('Tales')
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = "Cu"
teste[1] = '12'
galera.append(teste[:])
print(galera)
'''
#---------------------------------------------------------------------
'''
galera = [['B',19],['A', 20],['J', 22],['T', 20]]

print(galera)
print(galera[0][0])

for i in galera:
    print(f'nomes: {i[0]} e {i[1]} anos')
'''
#---------------------------------------------------------------------
'''
galera = []
dado = []
for i in range(3):
    dado.append(input("Nome: "))
    dado.append(int(input("Idade: ")))

    galera.append(dado[:])
    dado.clear()

for j in galera:
    if j[1] >= 20:
        print(f"Apenas os de maiores: {j[0]}")
    else:
        print(f"De Menores: {j[0]}")
'''

                                                                #DESAFIOS

# 1 -> ler nome e peso de varias pessoas, quantas pessoas cadastradas, listagem das mais pesadas, listagem das mais leves
'''
galera = []
dados = []
maior = 0
menor = 999
qnt = 0
pesado =''
leve =''

while True:
    nome = input("Nome: ")
    peso = int(input("Peso: "))

    dados.append(nome)
    dados.append(peso)
    galera.append(dados[:])
    dados.clear()

    qnt +=1

    if peso > maior:
        maior = peso
        pesado = nome

    if peso < menor:
        menor = peso
        leve = nome

    resposta = input("Deseja continuar ? [s/n]").lower()
    if resposta != 's':
        break
    else:
        print('Cadastrada ...')


for i in galera:
    print(f"Pessoas registradas: {galera}")
    
print(f"quantidade: {qnt}")

print(f"Maior Peso: {pesado} com {maior} KG")
print(f"Mais leve {leve} com {menor} KG")
'''

# 2 -> digitar sete valores, cadastrar em uma lista (vao ter duas dentros) e separar em pares e impares e em ordem crescente
'''
num = [[],[]]

valor = 0

for i in range (7):
   
   valor = int(input(f"Valor {i}: "))
   if valor % 2 == 0:
      num[0].append(valor)
    
   else:
      num[1].append(valor)

print(f'Valores: {num}')
num[0].sort()
num[1].sort()

print(f'Pares: {num[0]}')
print(f'Impares: {num[1]}')
'''

# 3 -> criar uma matriz 3x3, mostrar a matriz com formatação
'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
valor = 0

for i in range (3):
    for j in range (3):
        matriz[i][j] = int(input(f"Valor de [{i},{j}]: "))

print('-=' * 30)
for k in range (3):
    for l in range (3):
        print(f'[{matriz[k][l]}]')
'''
# 4 aprimorar a matriz, mostrano a soma , soma terceira coluna, maior da segunda linha
'''
soma1 = soma2 = maior = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range (3):
    for j in  range (3):
        matriz[i][j] = int(input(f"Valor de {i}{j}: "))

        soma1 += matriz[i][j]

        soma2 += matriz[i][2]

        if matriz[1][j] > maior:
            maior = matriz[1][j]

print(f"Soma total: {soma1}")
print(f"Soma da terceira coluna: {soma2}")
print(f"Maior valor da segunda linha: {maior}")

print("\nMatriz:")
for i in range(3):
    for j in range(3):
        print(f"{matriz[i][j]:^5}", end='')
    print()
'''

# 5 -> criador de palpite MEGA SENA 
'''
from random import randint

jogos = []

qnt = int(input("Quantos jogos quer jogar? "))

while qnt > 0:
    lista = []
    cont = 0

    while cont < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1

    lista.sort()
    jogos.append(lista[:])
    qnt -= 1

print("\nSeus palpites:")
for i, jogo in enumerate(jogos):
    print(f"Jogo {i+1}: {jogo}")
'''

# 6 -> ler nome e duas notas, no final mostre um boletim com a media e a nota de cada um
ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = int(input('N1: '))
    nota2 = int(input('N2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])

    resp = input("Deseja continuar ? [s/n]").lower()

    if resp != 's':
        break
    else:
        print("Registrado...")

print(f"{'N.':<4}{'Aluno':<15}{'Média':>8}")
print("-" * 30)

for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<15}{a[2]:>8.1f}")




     


    





