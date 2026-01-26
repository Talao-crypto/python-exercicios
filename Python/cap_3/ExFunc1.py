#1 Calcular a area de um terreno retangular 
'''
def calc (a,b,):
    r = a*b
    return r

def main():
    print("Calculo de Terreno")
    print("-="*15)

    n1 = float(input("Largura: (m)"))
    n2 = float(input("Comprimento: (m)"))

    resultado = calc(n1,n2)
    
    print(f"Largura: {n1} Comprimento: {n2} Area esperada: {resultado}")

main()
'''

#2 Uma função chamada escreva (recebe um texto) mostrar na tela com tamanho adapitavel
'''
def texto(txt):
    tam = len(txt)
    print("-" *tam)
    print(f'{txt}')
    print("-" *tam)


def main():
    

    texto('Tales')

    
    texto('Curos em Video Guanabara ')

main()
'''

#3 FUNÇAO CONTADOR RECEBE 3 PARAMETROS, INICIO FIM PASSO, A) DE 1 A 10 EM 1 B) DE 10 A 0 EM 2 C) PERSONALIZADO
'''
from time import sleep

def contador(inicio, fim, passo):
    atual = inicio

    if inicio > fim:
        while atual >= fim:
            print(atual, end=" ", flush=True)
            atual -= passo
            sleep(0.5)
    else:
        while atual <= fim:
            print(atual, end=" ", flush=True)
            atual += passo
            sleep(0.5)

    print("FIM")


def main():
    n1 = int(input("Início: "))
    n2 = int(input("Fim: "))
    n3 = int(input("Passo: "))

    if n3 == 0:
        n3 = 1

    n3 = abs(n3)

    print(f"Contagem de {n1} até {n2} de {n3} em {n3}")
    contador(n1, n2, n3)


main()
'''

#4 DESEMPACOTAMENTO, RECEBER VARIOS PARAMETROS (FUNC MAIOR), ANALISAR TODOS OS VALORES E MOSTRAR O MAIOR
'''
from time import sleep

def maior(*num):
    print("Analisando Valores Passados:")
    sleep(0.5)

    maior = num[0]   # começa pelo primeiro valor

    for i in num:
        print(i, end=" ", flush=True)
        sleep(0.5)
        if i > maior:
            maior = i

    print()
    print(f"Foram informados {len(num)} valores ao todo")
    print("-=" *30)
    print(f"O maior foi: {maior}")
    print("-=" *30)


def main():
    print("Agora é sua vez!")
    print("Digite os números para serem analisados (digite 0 para parar)")

    numeros = []

    while True:
        n = int(input("Num: "))
        if n == 0:
            break
        numeros.append(n)

    if len(numeros) == 0:
        print("Nenhum informado")

    else:
        maior(*numeros)

main()
'''

#5 tenha uma lsita Num, uma função sorteia( vai sortear 5 num e colocar na lista), função somaPar (vai somar todos os pares da lista)
from random import randint

def sorteia(lista):

    for i in range (5):
        lista.append(randint(0,100))

def SomaPar(lista):
    soma = 0

    for i in lista:
        if i % 2 == 0:
            soma += i

    return soma

def main():
    Num = []
    sorteia(Num)

    print(f"Numeros Sorteados: {Num}")

    print(f"Soma dos Pares: {SomaPar(Num)}")


main()



