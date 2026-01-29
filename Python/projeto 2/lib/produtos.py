from lib.dados import carregar_produtos, salvar_produtos


def gerar_id(lista):
    if not lista:
        return 1
    return lista[-1]['id'] + 1


def cadastrar_produto(nome, categoria, quantidade, preco):
    produtos = carregar_produtos()

    novo_produto = {
        'id': gerar_id(produtos),
        'nome': nome,
        'categoria': categoria,
        'quantidade': quantidade,
        'preco': preco
    }

    produtos.append(novo_produto)
    salvar_produtos(produtos)


def status_estoque(quantidade):
    if quantidade == 0:
        return 'ACABOU'
    elif quantidade <= 5:
        return 'ACABANDO'
    else:
        return 'OK'


def repor_produto(id_produto, quantidade):
    produtos = carregar_produtos()

    for p in produtos:
        if p['id'] == id_produto:
            p['quantidade'] += quantidade
            break

    salvar_produtos(produtos)


def excluir_produto(id_produto):
    produtos = carregar_produtos()

    produtos = [p for p in produtos if p['id'] != id_produto]

    salvar_produtos(produtos)

    