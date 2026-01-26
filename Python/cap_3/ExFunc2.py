# 1 -> fun (voto) recebe o ano de nascimento (calcula idade) , retornar valor literal se ela pode votar ou nao 
'''
from datetime import datetime

def voto (nasci=0):
    idade = datetime.now().year - nasci
    print(f"Com {idade} anos seu voto é: ")

    if idade < 16:
        return print("Negado")
    elif idade >= 18:
        return print("Obrigatorio")
    else:
        return print("Opicional")
    
def main():
    n = int(input("Digite o ano de nascimento: "))
    voto(n)

main()
'''

# 2 -> fun (fatorial) recebe 1 num e um show(se quer ou n a conta na tela)
'''
def fat (n=0,j=0):
    f = 1

    if j == 0:
        for i in range (n,0,-1):
            f*=i
            print(f'{i} x ', end="")

    elif j == 1:
        for i in range (n,0,-1):
            f*=i

   
    print(f"O fat de {n} é {f}")
    print("-=" *15)

def main():

    num = int(input("Num: "))

    resp = int(input("Digite 0 -> para mostrar o calculo, 1 -> apenas resultado"))

    fat(num,resp)

main()
'''

# 3 -> fun (ficha) recebe nome e quantos gols, mostrar a ficha do jogador mesmo se algum dado foi informado incorretamente
'''
def ficha(nome='<desconhecido>',gols=0):
    print(f"O jogador {nome} fez {gols} gols")
    


def main():
    n = input("Nome: ")
    g = input("Gols: ")

    if g.isnumeric():
        g=int(g)
    else:
        g=0
    if n.strip() == '':
        ficha(gols=g)
    else:
        ficha(n,g)

main()
'''

# 4 -> fun (leiaint) recebe um numero, so deve aceitar receber valor numerico 
'''
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("Digite um numero VALIDO")
        if ok:
            break
    return valor

n = leiaint('Digite num: ')
print(f"O num é {n}")
'''

# 5 -> func (notas) recebe varias notas, retornar um dicionario -> qnt de notas, maior nota, menor nota, media, situação
'''
from time import sleep

def notas(*n, sit=False):
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['média'] = sum(n)/len(n)

    if sit:
        if r['média'] >= 7.5:
            r['Situação'] = "Parabens"
        elif r['média'] >= 5:
            r['Situação'] = "Passou"
        else:
            r['Situação'] = "Pobre"

    return r

    
def main():

    lista = []

    while True:
        n = float(input("Nota: "))

        lista.append(n)

        resp = input("Deseja continuar ?").lower()

        if resp != 's':
            break

        print("Registrando")
        sleep(0.5)
        print("...")
    
    form = notas(*lista, sit=True)
    print(form)

main()
'''


# 6 -> fazer um sistema q utiliza o interactive help
'''
from time import sleep

def ajuda(com):
    print("\033[42m" + "-" * 40)
    print(f"Acessando a documentação de '{com}'".center(40))
    print("-" * 40 + "\033[m")
    sleep(1)
    help(com)


while True:
    print("\033[44m" + "=" * 40)
    print("  SISTEMA DE AJUDA PyHELP".center(40))
    print("=" * 40 + "\033[m")

    comando = input("Função ou Biblioteca (Digite 'FIM' para sair): ").strip()

    if comando.upper() == "FIM":
        print("\033[41m" + "-" * 40)
        print("Encerrando o sistema...".center(40))
        print("-" * 40 + "\033[m")
        break
    else:
        ajuda(comando)
'''

# 7 -> func (cadastre) -> recebe nome,idade, sexo (m/f)
# cada pessao armazenada em um dicionario, devem ser guardados em uma lista
# mostrar qnt, media idade, lista mulheres, pessoas acima da medai de idade
from time import sleep

def cadastro():
    r = {}
    r['NOME'] = input("Nome: ").upper()
    r['IDADE'] = int(input("Idade: "))
    r['SEXO'] = input("SEXO: [M/F]").upper()

    return r

def analisar(galera):
    print("-=" *30)
    print(f"Total de Pessoas analisadas: {len(galera)}")

    soma_idade = 0
    mulheres = []
    acima_idade = []

    for p in galera:
        soma_idade += p['IDADE']
        if p['SEXO'] == 'F':
            mulheres.append(p['NOME'])
    
    media = soma_idade/len(galera)

    print(f"Media da idade: {media}")

    print("Mulheres Cadastradas: ")
    for m in mulheres:
        print(m, end=" ")
    print()

    print("Pessoas Acima da Media de Idade: ")
    for p in galera:
        if p['IDADE'] > media:
            print(p['NOME'], end=" ")
    print()

def main():
    galera = []

    while True:
        pessoa = cadastro()
        galera.append(pessoa.copy())

        resp = input("Deseja Continuar ? [s/n]").strip().upper()
        while resp not in 'SN':
            resp = input("Digite um caracter Valido")
        if resp == 'N':
            break

        print("Registrando ...")
        sleep(0.5)

    analisar(galera)

main()







    

    
    