'''
nome = str(input("Qual seu nome ?"))
if nome == 'Tales':
    print("FODA")

elif nome == 'Roger':
    print("Foda")

else:
    print("FOTO DO CU")

print("Tenha um bom dia {}".format(nome))
'''


# EXERCICIO 1 APROVAR UM EMPRESTIMO PERGUNTA SALARIO VALOR DA CASA EM QUANTOS ANOS ELA VAI PAGAR, CALCULAR A PRESTAÇÃO MENSAL(N PODE PASSAR DE 30% DO SALARIO)
'''
salario = int(input("Salario: "))
casa = int(input("Valor casa: "))
prestacao = int(input('Quantos anos de prestações: '))
prestacao * 12

prestacao_mensal = casa / prestacao

if prestacao_mensal > salario*0.3:
    print("Emprestimo Negado")
else:
    print("Emprestimo liberado")
'''

# EXERCICIO 2 USUARIO VAI ESCREVER UM NUMERO E DEVE ESCOLHER A BASE DE CONVERÇÃO
'''
def main():
    num = int(input("Digite o número: "))
    opcao = int(input("Escolha a base:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\nOpção: "))

    if opcao == 1:
        print(f"Binário: {bin(num)[2:]}")
    elif opcao == 2:
        print(f"Octal: {oct(num)[2:]}")
    elif opcao == 3:
        print(f"Hexadecimal: {hex(num)[2:]}")
    else:
        print("Opção inválida")


if __name__ == "__main__":
    main()
'''

# EXERCICIO 3 LER DOIS NUM VER QUAL E MAIOR
'''
num1=int(input("Num: "))
num2=int(input("Num: "))

if num1>num2:
    print("Numero {} maior que o {}".format(num1,num2))

elif num2>num1:
    print("Numero {} maior que {} ".format(num2,num1))

else:
    print("Iguais {}".format(num2))
'''

# EXERCICIO 4 LEIA O ANO -> VAI SE ALISTAR, -> HORA DE SE ALISTAR, -> PASSOU O TEMPO

'''
idade = int(input("ANOS DE NASCIMENTO: "))

alistamento = 2025 - idade

if alistamento < 18 :
    print("ainda vai se alistar")
    tempo = 18 - alistamento
    print("ainda falta {} anos".format(tempo))
elif alistamento == 18:
    print("hora de se alistar")
else:
    print("Passou o tempo")
    tempo = alistamento - 18
    print("Passou {} anos " .format(tempo))
'''

# EXERCICIO 5 CALCULAR MEDIA
'''
n1 = float(input("P1: "))
n2 = float(input("P2: "))
n3 = float(input("P3: "))

media = (n1*0.3) + (n2*0.3) + (n3*0.4)

if media < 5:
    resposta = input("Vai querer fazer rec ? (s/n) ")

    if resposta == 's':
        prova = input("Qual prova quer substituir ? (n1,n2,n3) ")

        n4 = float(input("NOTA: "))

        if prova == 'n1':
            media = (n4*0.3) + (n2*0.3) + (n3*0.4)
        elif prova == 'n2':
            media = (n1*0.3) + (n4*0.3) + (n3*0.4)
        elif prova == 'n3':
            media = (n1*0.3) + (n2*0.3) + (n4*0.4)
        else:
            print("Caracter inválido")
            exit()

        print(f"Média final: {media:.2f}")

        if media >= 5:
            print("APROVADO")
        else:
            print("REPROVADO")
else:
    print("APROVADO")
'''

# EXERCICIO 6 LER ANO DE NASCIMENTO E MOSTRAR CATEGORIA
'''
ano = int(input("Ano de nascimento: "))

idade = 2025 - ano

if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print("JUNIOR")
elif idade <= 25:
    print("SENIOR")
else:
    print("VAI TOMA NO CU")
'''

# EXERCICIO 7 LER PESO E ALTURA (IMC) E MOSTRAR SATUS
'''
peso = float(input("Seu peso: "))
altura = float(input("Altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("MTO LEVINHO VAI VOAR")

elif imc <= 25:
    print("NORMAL")

elif imc <= 30:
    print("GORDIN")

else:
    print("Q GORDAO FILHA DA PUTA BATEU NA PUTA DE KENNER, GORDAO CANALHA")
'''

# EXERCICIO 8 METODO DE PAGAMENTO DE UM PRODUTO: DINHEIRO/CHEQUE = 10% DESCONTO, 2X 5% DE DESCONTO (CARTAO), 3x OU MAIS 20% DE JUROS
'''
preco = float(input("Digite o preço do produto: "))

metodo = int(input("1: dinheiro/cartao  2: cartao a vista  3: parcelado em 2  4:  3 vezes ou mais"))

if metodo == 1:
    desconto = preco * 0.1
    preco_final = preco - desconto
    print("DE {} POR {}".format(preco, preco_final))

elif metodo == 2:
    desconto = preco*0.05
    preco_final = preco - desconto
    print("DE {} POR {}".format(preco, preco_final))

elif metodo == 3:
    preco_final = preco / 2
    print("DUAS PARCELAS DE {}".format(preco_final))

elif metodo == 4:
    juros = preco * 0.2

    vezes = int(input("Quantas vezes voce quer fazer: "))

    preco_final = preco + (juros * vezes)

    print("VALOR FINAL {} EM {} VEZES ".format(preco_final, vezes))


else:
    print("invalido")
'''

# EXERCICIO 9 FAZER UM JOCKENPO
import random

minha_escolha=input("PEDRA, PAPEL, TESOURA").upper()

opcoes=["PEDRA", "PAPEL", "TESOURA"]
escolha_maquina=random.choice(opcoes)

print(f"Você: {minha_escolha}")
print(f"Máquina: {escolha_maquina}")

if minha_escolha == escolha_maquina:
    print("Empate!")
elif (
    (minha_escolha == "PEDRA" and escolha_maquina == "TESOURA") or
    (minha_escolha == "PAPEL" and escolha_maquina == "PEDRA") or
    (minha_escolha == "TESOURA" and escolha_maquina == "PAPEL")
):
    print("Você ganhou!")
else:
    print("Você perdeu!")















