def soma (a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "Erro: div por 0"
    return a/b

# ==============
# Menu

def menu():
    print("\nOpções:")
    print("1- soma")
    print("2- sub")
    print("3- mult")
    print("4 div")
    print("0 sair")

# ==============
# Main

def main():
    nome = input("Nick: ")
    print(f"\nCalculadora do {nome}")

    while True:
        menu()
        opcao=input("Opção: ")

        if opcao=="0":
            print("Encerrando Programa")
            break
        

        a=float(input("N1: "))
        b=float(input("N2: "))

        #switch case

        match opcao:
            case "1":
                resultado=soma(a,b)
            case "2":
                resultado=sub(a,b)
            case "3":
                resultado=mult(a,b)
            case "4":
                resultado=div(a,b)
            case _:
                resultado="invalido"
            
        print("Resultado", resultado)

if __name__=="__main__":
    main()
