from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'tales.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['LISTAR CADASTROS', 'NOVO CADASTRO', 'SAIR'])

    if resposta == 1:
        lerArquivo(arq)

    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ').strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        print()
        print(f'\033[32m✔ Cadastro de {nome} realizado com sucesso!\033[m')

    elif resposta == 3:
        cabeçalho('SAINDO DO SISTEMA')
        print('\033[31mFinalizando...\033[m')
        break

    else:
        print('\033[31mOpção inválida! Tente novamente.\033[m')

    sleep(0.7)
