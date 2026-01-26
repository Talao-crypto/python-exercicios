def mostrar_menu():
    print("1- cadastrar")
    print("2- listar pessoas")
    print("3- buscar pessoas")
    print("4- remover")
    print("0- sair")

def cadastrar(lista):
    nome = input ("Nome: ")
    idade = int(input("Idade: "))

    #struct 
    pessoa= {
        "nome": nome,
        "idade": idade
    }

    lista.append(pessoa) #coloca no final da lista
    print("Concluido !!")

def listar(lista):
    if len(lista) == 0:
        print("lista vazia")
        return
    for i,pessoa in enumerate(lista):
        print(f"{i}-{pessoa['nome']} ({pessoa['idade']} anos)")



def buscar(lista):
    nome_busca = input("Nome para buscar: ")

    for pessoa in lista:
        if pessoa["nome"] == nome_busca:
            print(f"Encontrado: {pessoa['nome']} - {pessoa['idade']} anos")
            return

    print("Pessoa não encontrada.")


def remover(lista):
    listar(lista)
    indice = int(input("Índice para remover: "))

    if 0 <= indice < len(lista):
        removida = lista.pop(indice)
        print(f"{removida['nome']} removido(a).")
    else:
        print("Índice inválido.")

def main():
    pessoas= []

    while True:
        mostrar_menu()
        opcao=input("Opção: ")

        match opcao:
            case "1":
                cadastrar(pessoas)
            case "2":
                listar(pessoas)
            case "3":
                buscar(pessoas)
            case "4":
                remover(pessoas)
            case "0":
                print("......")
                break
            case _:
                print("Invalido")

if __name__ == "__main__":
    main()        