def linha(tam = 15):
    return '-=' * tam

def leiaInt(msg):

    while True:
        try:
            n=int(input(msg))
        except(ValueError,TypeError):
            print("Caracter Invalido")
            continue
        else:
            return n
        

def cabeçalho(txt):
    print(linha())
    print(txt)
    print(linha())

def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc