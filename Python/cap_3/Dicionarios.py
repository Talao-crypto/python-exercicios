# personalizar os indices -> {} simbolo
# dados = {}
#dados = {'nome': Pedro, 'idade': 25} -> dados "0" == dados 'nome'

#adicionar elemento
#dados['sexo'] = 'M'

#remover elemento
#del dados['idade']

#print(dados.values()) -> mostra os valores de todas as seções
#print(dados.keys()) -> mostra os nomes q vc deu para a seção
#print(dados.items()) -> mostra o valor e o nome das seções
#--------------------------------------------------------------------------------------------------
                                                                #PRATICA
#--------------------------------------------------------------------------------------------------

# 1 

'''
pessoas = {'nome': 'Tales', 'sexo': 'M', 'idade': 20}
print(pessoas)
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

del pessoas['sexo']
print(pessoas)
'''

# 2

'''
pessoas = {'nome': 'Ana', 'sexo': 'F', 'idade': 21}

print('-=' *15)

for k in pessoas.values():
    print(k)

print('-=' *15)

for v in pessoas.keys():
    print(v)

print('-=' *15)

pessoas ['nome'] = 'Sofia'
pessoas ['peso'] = 57.9

for i,j in pessoas.items():
    print(f'{i} = {j}')
'''

# 3
'''
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil = []
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
'''
#4
'''
estado = {}
brasil = []

for i in range (2):
    estado['uf'] = input("Unidade Federativa: ")
    estado['sigla'] = input("Sigla: ")
    brasil.append(estado.copy())

for i in brasil:
    for k,j in i.items():
        print(f'O campo {k} tem valor {j}')
'''

#--------------------------------------------------------------------------------------------------
                                                                    #DESAFIO
#--------------------------------------------------------------------------------------------------

# 1 -> perguntar nome e a media, guardar em um dicionario
'''
boletim = {}

boletim['Nome'] = input("Nome: ")
boletim['Media'] = float(input(f'Media de {boletim["Nome"]}: '))

print(f"O nome é: {boletim['Nome']}")
print(f"Media igual a: {boletim['Media']}")

if boletim['Media'] >= 5:
    print("Aprovado")
else:
    print("Reprovado")
'''

# 2 -> 4 jogadores jogam um dado, tendo resultados aleatorios e guardar em um dicionario, coloque em ordem e o vencedor e o maior numero
'''
from random import randint
from time import sleep
from operator import itemgetter 

maior = 0

jogo = {'P1': randint(1,6),
        'P2': randint(1,6),
        'P3': randint(1,6),
        'P4': randint(1,6)
        }

rankin = []

print("Valores Sorteados")

for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(0.5)

rankin = sorted(jogo.items(), key = itemgetter(1),reverse=True)

for i, j in enumerate(rankin):
    print(f'{i+1} lugar: {j[0]} com {j[1]}')
    sleep(0.5)
'''

# 3 -> ler nome,ano de nascimento, carteira de trabalho, (guarda a idade)
'''
from datetime import datetime
aposentadoria = {}

aposentadoria['Nome'] = input("Nome: ")
nasc = int(input("Ano de nascimento: "))

aposentadoria['idade'] = datetime.now().year - nasc

aposentadoria['Carteira'] = int(input("Carteira de Trabalho: "))

if aposentadoria['Carteira'] != 0:
    aposentadoria['contratação'] = int(input("Ano de contratação: "))
    aposentadoria['Salario'] = float(input("Salario: "))

    aposentadoria['Aposentar'] = aposentadoria['idade'] + ((aposentadoria['contratação'] + 35) - datetime.now().year)

for k, v in aposentadoria.items():
    print(f"{k} tem valor {v}")
'''

# 4 -> ler nome,quantas partidas, quantidade de gols em cada partida, guardar o aproveitamento dele
'''
jogador = {}
partidas = []

jogador['nome'] = input("Nome do Jogador: ")
tot = int(input(f"Partidas jogadas do {jogador['nome']}: "))

for i in range (tot):
    partidas.append(int(input(f"Gols na Partida {i+1}: ")))

jogador['Gols'] = partidas[:]
jogador['total'] = sum(partidas)

print("-=" * 30)



for k,v in jogador.items():
    print(f"O campo {k} tem valor {v}")
'''

# 5 -> ler nome,sexo de varias pesssoas, guardar em uma lista todas as pessaos, A) quantas pessoas foram cadastradas, B) media de idade, C) uma lista com as mulheres, D) uma lista com todas as pessaos acima da media
'''
pessoa = {}
galera = []

qnt = soma = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = input("Nome: ")
    pessoa['Sexo'] = input("Sexo [f/m]: ").lower()
    pessoa['Idade'] = int(input("Idade: "))

    qnt += 1
    soma += pessoa['Idade']

    galera.append(pessoa.copy())

    resp = input("Deseja continuar? [s/n] ").lower()
    if resp != 's':
        break

media = soma / qnt

print("-=" * 30)
print(f"Total de pessoas: {qnt}")
print(f"Média de idade: {media:.1f}")

print("\nMulheres cadastradas:")
for p in galera:
    if p['Sexo'] == 'f':
        print(p['Nome'])

print("\nPessoas acima da média de idade:")
for p in galera:
    if p['Idade'] >= media:
        print(p['Nome'])
'''








