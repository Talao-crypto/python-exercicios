'''
def main():
    ano = int(input("Quantos anos tem seu carro ? "))

    if ano <= 3:
        print("Novo")
    elif ano <= 5:
        print("Semi-novo")
    else:
        print("Velho")


if __name__ == "__main__":
    main()  

'''


''' 
nome = str(input("Nome: "))
if nome==   'tales' :
    print("MOSTRA O CU")
print("Bom dia, {} ".format(nome))
'''

'''
n1 = float(input("N1: "))
n2 = float(input("N2: "))

media=(n1+n2)/2

print ("Sua media foi: {:.1f}" .format(media))

if media >= 8:
    print("Amassou")
elif media >= 5:
    print("Passou")
else:
    print("KKKKKKKKKKKKKKKKKKKKKKKKK")
'''

# EXERCICIO 1 JOGO DE ADIVINHAR
'''
import random

def main():
    numero_secreto = random.randint(0, 5)
    tentativas = 0

    while True:
        chute = int(input("Tente adivinhar o número (0 a 5): "))
        tentativas += 1

        if chute == numero_secreto:
            print("Parabéns, você acertou!")
            break
        else:
            print("Errou, tente novamente.")

    print(f"Você tentou {tentativas} tentativas.")


if __name__ == "__main__":
    main()
'''

# EXERCICIO 2 RADAR (PASSOU DE 80 TOMA MULTA DE 7 PARA CADA KM A CIMA DO LIMITE)
'''
import random 
def main():
    vel=random.randint(60,120)

    if vel>80:
        acima = vel - 80
        multa = 7 * acima
        print("MULTADO SUA VEL: {}" .format(vel))
        print("VALOR {}".format(multa))

        
    elif vel >= 70:
        print("CUIDADO LIMITE 80")

    else:
        print("De boas")

if __name__ == "__main__":
    main()
'''


# EXERCICIO 3 PREÇO VIAGEM DE ONIBUS
'''
def main():

    distancia=float(input("DISTANCIA DE VIAGEM"))
    valor=0

    if distancia<= 200:
        valor = 0.5 * distancia
    else:
        valor = 0.45 * distancia
    
    print("Valor total: {}".format(valor))


if __name__ == "__main__":
    main()
'''

# EXERCICIO 4 MOSTRAR O MAIOR E O MENOR

'''
def main():

    n1=int(input("num: "))
    n2=int(input("num: "))
    n3=int(input("num: "))

    maior =0
    menor =99999999999999999

    if n1>maior:
        maior = n1
    if n2>maior:
        maior = n2
    if n3>maior:
        maior = n3

    if n1<menor:
        menor=n1
    if n2<menor:
        menor=n2
    if n3<menor:
        menor=n3
    
    print("menor: {}" .format(menor))
    print("maior: {}".format(maior))
if __name__ == "__main__":
    main()
'''

# EXERCICIO 4 MAS DIFERENTE
'''
def main():

    numeros=[]

    for i in range(3):
        n=int(input("Num: "))
        numeros.append(n)
    
    maior=numeros[0]
    menor=numeros[0]

    for n in numeros:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    print(f"menor: {menor}")
    print(f"maior: {maior}")


if __name__ == "__main__":
    main()
'''

#EXERCICIO 5 CALCULAR AUMENTO DE SALARIO (SUPERIPR A 1.250 AUMENTO DE 10%) (INFERIORES OU IGUAIS 15%)

def main():

    salario = int (input("Salario Atual: "))

    if salario>1250:
        aumento = salario * 0.10
    else:
        aumento = salario * 0.15
    
    salario_atual=salario+aumento

    print("Seu aumento foi de {}".format(aumento))
    print("\n Seu salario novo sera: {}".format(salario_atual))

if __name__ == "__main__":
    main()

