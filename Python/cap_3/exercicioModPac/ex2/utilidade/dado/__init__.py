def leiaDinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("Digite um Valor Válido para continuar")
        if ok:
            break
    return valor