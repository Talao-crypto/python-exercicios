def aumente(n=0,k=0,par=False):
    por = (k*n) / 100
    return (n + por) if par is False else moeda(n+por)



def diminuir(n=0,l=0,par=False):
    por = (n*l) / 100
    return (n - por) if par is False else moeda(n-por)



def dobro(n=0,par=False):
    return (n*2) if par is False else moeda(n*2)



def metade(n=0,par=False):

    return (n/2) if par is False else moeda(n/2)




def moeda(n=0,):
    return f'R$ {n}'.replace('.',',')



def resumo(n,aumento=0,desconto=0):
    print("--" *15)
    print("TABELA")
    print("--" *15)

    print(f"Preço analisado: {n}")
    print(f"Dobro: {dobro(n,True)}")
    print(f"A metade: {metade(n,True)}")
    print(f"Com 80% de aumento: {aumente(n,80,True)}")
    print(f"Com 37% de desconto: {diminuir(n,37,True)}")
    print("--" *15)
    

    