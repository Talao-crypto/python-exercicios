# Variavel composta 
# variaveis q armazenam mais de um valor (semelhante a uma lista)
# TUPLA É IMUTAVEL -> N PODE AICIONAR / REMOVER VALORES

'''
ESTRUTURAS
len(lanches) -> tamanho da lista

for c in lanche:
    print(c) -> vai imprimir a lista

'''

'''
FATIAMENTOS 

print(lanche [2]) -> mostra so o item 2 
print(lanche [0:2]) -> mostra os itens 0 e 1 (ignora o 2)
print(lanche [1:]) -> começa do 1 ate o final 
print(lanche [-1]) -> o primeiro de traz para frente

'''

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    #PRATICA
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
lanche = ('lanche', 'suco', 'pizza', 'pudim')
print(lanche)
print(lanche[1])
print(lanche[0:3])
print(lanche[2:])
print(lanche[-3]) -> mostra so essa pos especifica
print(lanche[-1:]) -> vai ate o final

'''

'''
lanche = ('lanche', 'suco', 'pizza', 'pudim')

for c in lanche:
    print(f'vou comer {c}')
print("enchi")

for cont in range(0,len(lanche)):
    print(f'agora comi {lanche[cont]} na posição {cont}')
print("enchi")

print(sorted(lanche))  -> coloca em ordem
'''

'''
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print (c)
print(sorted(c))
print(len(c))
print(c.count(2))
print(c.index(8)) #posição do valor 8
del(b) #deleta
'''

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    #DESAFIOS
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# EXERCICIO 1 -> UMA TUPLA DE 0 A 20, E ESCREVE O NUMERO Q ELE DIGITOU MAS EM EXTENSO
'''
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 
            'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input("Num de 0 a 20: "))

    if 0 <= num <= 20:
        break
    
    print("invalido")

print(f"O numero é: {contagem[num]}")
'''

# EXERCICIO 2 -> UMA TUPLA DE 20, -> 5 PRIMEIROS, -> ULTIMOS 4, -> LISTA EM ORDEM ALFABETICA, -> EM Q POS TA O CORINTHIANS
'''
tabela_2024 = (
    'Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
    'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco',
    'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude',
    'RB Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá'
)

print(f"Os 5 primeiros foram: {tabela_2024 [0:5]} \n")
print(f"As ultimas 4 colocações foram: {tabela_2024 [-4:]} \n")
print(f"Ordem alfabetica: {sorted(tabela_2024)} \n")
print(f"E o timão ficou em: {tabela_2024.index('Corinthians')+1}")
'''

# EXERCICIO 3 -> gerar 5 aleatorios e colocar na tupla, -> mostrar os numeros gerados, indicar maior e menor valor da tupla
'''
import random

numeros = (random.randint(0,100) , random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100))
maior = 0
menor = 999
for c in range (0,len(numeros)):
    print(f"Numero {c}: {numeros[c]}")

    if numeros[c] > maior:
        maior = numeros[c]
    
    if c < numeros[c]:
        menor = numeros[c]

print(f"Maior Valor: {maior}, Menor Valor: {menor}")
'''

# EXERCICIO 4 -> ler 4 valores, -> qnt de 9, posição do primeiro valor 3, -> numeros pares quais foram
'''
num1 = int(input("Digite: "))
num2 = int(input("Digite: "))
num3 = int(input("Digite: "))
num4 = int(input("Digite: "))

numeros = (num1,num2,num3,num4)

qnt9 = 0

for c in range (len(numeros)):

    if numeros[c] == 9:
        qnt9 += 1
    
    if numeros[c] % 2 == 0:
        print(f"Par {c}: {numeros[c]}")
    
if 3 in numeros:
    print(f"Posição: {numeros.index(3)}")
else:
    print("N existe")
'''

# EXERCICIO 5 -> uma tupla com nomes e preço de produtos e imprimir uma tabela dos preços
'''
produtos = (
    "Lápis", 1.50,
    "Caderno", 15.90,
    "Borracha", 2.00,
    "Mochila", 120.00,
    "Caneta", 3.50,
    "Livro", 45.00
)
print("LISTAGEM")

print("LISTAGEM DE PREÇOS")

for c in range(len(produtos)):
    if c % 2 == 0:
        print(f"{produtos[c]:.<30}", end='')
    else:
        print(f"R${produtos[c]:>10.2f}")
'''

# EXERCICIO 6 -> TUPLRA COM PALAVRAS, MOSTRAR PARA CADA PALAVRA SUAS VOGAIS

palavras = ('arroz', 'cadeira', 'escova', 'sexo', 'placa', 'peitos')

for c in palavras:
    print(f"Palavra: {c} vogais: ", end='')

    for i in c:              # ← AQUI foi a correção
        if i in "aeiou":
            print(i, end=' ')
    print()











