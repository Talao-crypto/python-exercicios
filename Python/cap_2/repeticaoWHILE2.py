# No python n tem -> Do While

'''

while True:
    codigod ....
    codigod ....
    codigod ....
    if (condicao):
        break:

'''

'''
n = s = 0

while True:
    n = int(input("Num: "))
    if n == 999:
        break
    s += n

print(f"soma: {s}")

'''

# EXERCICIO 1 -> ler varios nuemeros, so para quando digitar 999, mostrar a soma e a quantidade de numeros
'''
n = s = q = 0

while True:
    n = int(input("Num: "))
    if n == 999:
        break
    s += n
    q += 1

print(f"Soma: {s} Quantidade: {q}")
'''

# EXERCICIO 2 -> MOSTRAR A TABUADA DO NUMERO DIGITADO, DEVE PARA QUANDO FOR NEGATIVO
'''
n = 0

while True:
    n = int(input("Tabuada de qual valor ? "))

    if n < 0:
        break

    c = 0
    t = 0

    while c <= 10:
        t = n * c
        print(f"{n} * {c} = {t}")
        c += 1
print("Fim")
'''

# EXERCICIO 3 -> JOGAR PAR OU IMPAR COM O COMPUTADOR, SO ACABA QUANDO O JOGADOR PERDER, MOSTRAR A QUANTIDADE DE VITORIAS ATE PERDER
'''
import random

v = 0

while True:
    resposta = input("Par ou Impar ? [par/impar]").lower()

    if resposta not in ("par", "impar"):
        print("invalida")
        continue

    n1 = int(input("num: "))
    n2 = random.randint(0,20)
    s = n1 + n2

    if resposta == 'par':

        if s % 2 == 0:
            v+=1
            print("Ganhou")
        else:
            break
    else:
        
        if s % 2 != 0:
            v+=1
            print("Ganhou")
        else:
            break

print(f"vitorias: {v}")
'''

# EXERCICIO 4 -> ler idade e sexo, perguntar se a pessoa quer cotinuar, quantas > 18, homens, mulheres < 20
'''
qh = qm = q = 0


while True:
    print("CADESTRE: ")

    idade = int(input("Sua Idade: "))
    sexo = input("Sexo: [H/M]").upper()

    if sexo not in ("H","M"):
        continue

    if idade >= 18:
        q+=1
    
    if sexo == 'H':
        qh += 1

    if sexo == 'M':
        if idade <= 20:
            qm += 1


    continuar = input("Deseja continuar  ? [s/n]").lower()

    if continuar not in ("s","n"):
        continue

    if continuar == 'n':
        break


print(f"Maiores: {q}, Homens: {qh}, Mulheres menores de 20: {qm}")
'''

# EXERCICIO 5 -> ler nome, preço, quer continuar, total gasto, produtos acima de 200, nome do mais barato
'''
g = acima = 0
brt = ""
brt2 = 99999

while True:
    nome = input("Nome produto: ").upper()
    p = int(input("Preço: "))

    g += p

    if p > 200:
        acima += 1

    if p < brt2:
        brt2 = p
        brt = nome   

    resposta = input("Tem mais produtos? [s/n] ").lower()

    if resposta not in ("s", "n"):
        continue
    if resposta == "n":
        break

print(f"Valor total: {g}")
print(f"Acima de 200: {acima}")
print(f"Produto mais barato: {brt}")
'''

# EXERCICIO 6 -> VALOR Q IRA SACAR, INFORMAR QUANTAS CEDULAS SERAO ENTREGUES (50,20,10,1)
'''
valor = int(input("Valor sacar: "))
c = v = d = u = 0

while True:

    if valor == 0:
        break

    if valor >= 50:
        valor -= 50
        c += 1
    elif valor >= 20:
        valor -= 20
        v += 1
    elif valor >= 10:
        valor -= 10
        d += 1
    else:
        valor -= 1
        u += 1


print(f"Cédulas de 50: {c}")
print(f"Cédulas de 20: {v}")
print(f"Cédulas de 10: {d}")
print(f"Cédulas de 1: {u}")
'''





    







        



