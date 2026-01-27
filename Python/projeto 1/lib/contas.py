# saldo, saque, deposito


def ver_saldo(usuario):
    return usuario['saldo']

def depositar(usuario,valor):
    if valor <= 0:
        return False
    
    usuario['saldo'] += valor
    return True

def sacar(usuario,valor):
    if valor <= 0:
        return 0
    
    if valor > usuario['saldo']:
        print("Saldo insuficiente")
        return False
    
    usuario['saldo'] -= valor
    return True

def transferir(usuario_origem, usuario_destino, valor):
    if valor <= 0:
        return False, 'Valor inválido'
    
    if usuario_origem['saldo'] < valor:
        return False, 'Valor inválido'
    
    if usuario_origem['id'] == usuario_destino['id']:
        return False, 'Transferencia para mesma conta'
    
    usuario_origem['saldo'] -= valor
    usuario_destino['saldo'] += valor
    return True, 'TRANSFERENCIA REALIZADA...'