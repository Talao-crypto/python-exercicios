import random
from lib.dados import carregar_usuarios, salvar_usuarios

def email_existe(email, lista):
    for u in lista:
        if u['email'] == email:
            return True
    return False


def gerar_id(lista):
    ids_existentes = {u['id'] for u in lista}
    while True:
        novo_id = random.randint(0,200)
        if novo_id not in ids_existentes:
            return novo_id


def cadastrar_usuario(nome, email, senha):
    usuarios = carregar_usuarios()

    if email_existe(email, usuarios):
        return False

    novo_usuario = {
        'id': gerar_id(usuarios),
        'nome': nome,
        'email': email,
        'senha': senha,
        'saldo': 0.0
    }

    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    return True


def login_usuario(email, senha):
    usuarios = carregar_usuarios()

    for u in usuarios:
        if u['email'] == email and u['senha'] == senha:
            return u

    return None #N LOGOU

def buscar_usuario_por_email(email):
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u['email'] == email:
            return u
    return None
