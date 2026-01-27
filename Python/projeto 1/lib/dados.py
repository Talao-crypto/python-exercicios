# ler/escrever TXT

import os

ARQUIVO = 'banco.txt'

def carregar_usuarios():
    usuarios = []

    if not os.path.exists(ARQUIVO):
        open(ARQUIVO, 'w').close()
        return usuarios
    
    with open(ARQUIVO, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if linha == '':
                continue

            id_, nome, email, senha, saldo = linha.split(';')

            usuario = {
                'id': int(id_),
                'nome': nome,
                'email': email,
                'senha': senha,
                'saldo': float(saldo)
            }

            usuarios.append(usuario)
    return usuarios

def salvar_usuarios(lista):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        for u in lista:
            linha = f"{u['id']};{u['nome']};{u['email']};{u['senha']};{u['saldo']}\n"
            f.write(linha)

def atualizar_usuario(usuario_atualizado):
    usuarios = carregar_usuarios()

    for i,u in enumerate(usuarios):

        if u['id'] == usuario_atualizado['id']:
            usuarios[i] = usuario_atualizado
            break
    
    salvar_usuarios(usuarios)