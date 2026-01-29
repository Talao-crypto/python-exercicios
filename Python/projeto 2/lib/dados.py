import os

ARQUIVO = 'dados.txt'

def carregar_produtos():
    produtos = [] #lista

    if not os.path.exists(ARQUIVO):
        open(ARQUIVO, 'w').close()
        return produtos
    
    with open(ARQUIVO, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if linha == '':
                continue

            id_,nome,categoria,quantidade,preco = linha.split(';')

            produto = { #dicionario
                'id': int(id_),
                'nome': nome,
                'categoria': categoria,
                'quantidade': int(quantidade),
                'preco': float(preco)
            }

            produtos.append(produto)
    return produtos

def salvar_produtos(lista):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        for p in lista:
            linha = f"{p['id']};{p['nome']};{p['categoria']};{p['quantidade']};{p['preco']}\n"
            f.write(linha)

