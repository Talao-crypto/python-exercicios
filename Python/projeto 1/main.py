from lib.interface import menu, cabeçalho, leiaInt
from lib.usuarios import login_usuario, cadastrar_usuario, buscar_usuario_por_email
from lib.contas import ver_saldo, depositar,sacar,transferir
from lib.dados import atualizar_usuario

while True:
    opc = menu(['Login','Criar conta', 'Sair'])

    if opc == 1:
        email = input('Email: ')
        senha = input('Senha: ')
        usuario = login_usuario(email, senha)

        if usuario is None:
            print('Login inválido')
            continue

            # __LOGADO__

        while True:
            op = menu(['Ver saldo', 'Depositar','Sacar', 'Transferir', 'Logout'])

            if op == 1:
                cabeçalho('SALDO')
                print(f"Saldo atual: R$ {ver_saldo(usuario):.2f}")

            elif op == 2:
                valor = leiaInt('Valor para depósito: ')
                if depositar(usuario, valor):
                    atualizar_usuario(usuario)
                    print('Depósito realizado com sucesso')

            elif op == 3:
                valor = leiaInt('Valor de saque: ')
                if sacar(usuario,valor):
                    atualizar_usuario(usuario)
                    print('Saque realizado')
                else:
                    print("Saque invalido")
            elif op == 4:
                cabeçalho('Transferencia')

                email_destino= input('Email do destinatario: ').strip()
                usuario_destino = buscar_usuario_por_email(email_destino)

                if usuario_destino is None:
                    print("Usuario não existe")
                    continue

                valor = leiaInt('Valor R$: ')

                ok, msg = transferir(usuario,usuario_destino, valor)

                if ok:
                    atualizar_usuario(usuario)
                    atualizar_usuario(usuario_destino)
                    print(msg)
                else:
                    print(msg)
                
            elif op == 5:
                print('Logout realizado')
                break

    elif opc == 2:
        cabeçalho('CRIAR NOVA CONTA')
        nome = input('Nome: ')
        email = input('Email: ')
        senha = input('Senha: ')

        if cadastrar_usuario(nome,email,senha):
            print('Conta criada com sucesso...')
        else:
            print('Email ja em uso')

    elif opc == 3:
        print('Saindo...')
        break
    
    else:
        print("OPÇÃO INVALIDA")
