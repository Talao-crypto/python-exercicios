#listas usa [] e podem ser alteradas

# adicionar elementos -> (nome lista).append('valor')
# adicionar em posição desejada mexendo toda a lista -> (nome lista).insert(posição,'valor')
# adicionar -> push 


# remover -> (nome lista).pop(posição)  sem posição vc remove o ultimo
# remover -> (nome lista).remove('valor') 

# criando uma lista com range
# valores = list(range(4,11))

# valores = [8,2,5,4,3,0]

#organizar -> valores.sort()   ou valores.sort(reverse=True) ao contrario

#tamano -> len(valores)

                                            #PRATICA

'''
num = [2,3,5,7]
print(num)

num[0]=117
print(num)
num.append(7)
print(num)
num.insert(1,12312)
print(num)
num.sort(reverse=True)
print(num)


num.pop(2)
print(num)
num.remove(7)
print(num)
print(f"A lista esta com {len(num)} elementos ")
'''

'''
valores = []

for i in range(0,6):
    valores.append(int(input('Valor: ')))

for c,v in enumerate(valores):
    print(f"Na pos {c} encontrei o valor {v} ")
'''

#LIGAÇÃO MISTICA LISTAS
'''
a = [1,2,3,4,5]
b = a
b[2]=8

print(f'A: {a}')
print(f'B: {b}')
'''

#CRIANDO COPIA DE LISTA
'''
a = [1,2,3,4,5]
b = a[:]
b[2]=8

print(f'A: {a}')
print(f'B: {b}')
'''

                                                    #EXERCICIOS

# 1 -> ler 5 valores, mostrar o maior e o menor e sua posição na lista
'''
num = []
maior = 0
menor = 9999
pos=0
pos2=0

for i in range (5):
    num.append(int(input('Valor: ')))

    if num[i] > maior:
        maior = num[i]
        pos=i

    if num[i] <menor:
        menor = num[i]
        pos2=i

print(f"Maior valor: {maior} na posição {pos+1}")
print(f"Menor valor: {menor} na posição {pos2+1}")
'''

# 2 -> ler valores, caso ja exista n adicionar, mostar em ordem
'''
num = []
resposta = ''

while True:
    valor = int(input("Valor: "))

    if valor not in num:
        num.append(valor)
        print("Adicionado !!")
    else:
        print("Ja tem")
        
    resposta = input("deseja continuar ? [s/n]").lower()
    if resposta != 's':
        break

num.sort
print(f"Lista completa: {num}")
'''

# 3 -> ler varios, qnt digitados, decrescente e se o valor 5 foi digitado
'''
lista = []
qnt = 0
resp = ''

while True: 
    num = int(input("Valor: "))

    lista.append(num)
    qnt += 1

    resp = input("Continuar ? s/n").lower()

    if resp != 's':
        break

    if num == 5:
        print("Valor 5 digitado")

lista.sort(reverse=True) 
print(f"lista: {lista}")
print("Valor 5 n digitado")
'''

# 4 -> ler varios, criar 2 listas extras uma so com pares e outra so com impares
'''
lista = []
par = []
impar = []
resp = ''
while True:
    num = int(input("Valor: "))
    lista.append(num)

    if num % 2 == 0:
        par.append(num)
    if num % 2 != 0:
        impar.append(num)

    resp = input("Deseja continuar ? ")

    if resp != 's':
        break

print(f"Normal: {lista}")
print(f'Par: {par}')
print(f'Impar: {impar}')
'''








        




