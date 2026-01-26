#  INTERECTIVE HELP 
# help()

# digita: python e dps help(....), para sair usar o exit()


#DOCSTRING -> vc faz embaixo do def a explicação do codigo entre ''' .... '''
'''
def contador(i,j,k):
    
    -> FAZ UMA PA
    i = inicio
    j = fim
    k = passo
    
    c = i
    while c <= j:
        c += k
        print(c)

help(contador)
'''
            # PRATICA
# 1
'''
def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f

n = int(input("Num: "))
print(f"O fat é: {fatorial(n)}")
'''

# 2 
'''
def par (n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
def main():
    dopkapdokaw = int(input("Num: "))
    print(f"Numero é Par ? {par(dopkapdokaw)}")

main()
'''
