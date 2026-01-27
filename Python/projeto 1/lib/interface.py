from time import sleep


cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'verde': '\033[32m',
    'vermelho': '\033[31m',
    'amarelo': '\033[33m',
    'cinza': '\033[37m'
}


def linha(tam=50):
    return '-' * tam


def cabeçalho(txt):
    print(cores['azul'] + linha())
    print(txt.center(50))
    print(linha() + cores['limpa'])


def menu(opcoes):
    cabeçalho('MENU PRINCIPAL')
    for i, opc in enumerate(opcoes, start=1):
        print(f"{cores['amarelo']}{i}{cores['limpa']} - {opc}")
    print(linha())

    return leiaInt('Sua opção: ')


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(cores['vermelho'] + 'ERRO: Digite um número válido.' + cores['limpa'])
        else:
            return n


def msg_sucesso(msg):
    print(cores['verde'] + msg + cores['limpa'])
    sleep(0.6)


def msg_erro(msg):
    print(cores['vermelho'] + msg + cores['limpa'])
    sleep(0.6)


def msg_info(msg):
    print(cores['cinza'] + msg + cores['limpa'])
    sleep(0.5)
