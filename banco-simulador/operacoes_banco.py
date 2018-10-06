from limpa_tela import limpa_tela
from carrega_clientes import carrega
import menu
import json

def saldo(cliente):
    """Mostra saldo atual da conta em uso."""

    limpa_tela()
    print('SALDO DA CONTA'.center(30))
    print('=' * 30)
    print(f"SALDO ATUAL: R${cliente['saldo']:.2f}\n")
    input('Aperte ENTER para voltar...')
    menu.menu_usuario(cliente)

def deposito(cliente):
    """Simula um depósito na conta em uso."""
    cpf = cliente['cpf']
    limpa_tela()
    print('DEPOSITO EM CONTA'.center(30))
    print('=' * 30)
    dep = float(input('Valor do deposito: R$'))
    print()

    filename = 'contas/clientes'
    with open(filename) as file:
        clientes = json.load(file)

    for p, d in enumerate(clientes):
        if d['cpf'] == cpf:
            del clientes[p]

            if len(cliente['deposito']) < 10:
                cliente['deposito'].append(dep)
            else:
                cliente['deposito'].clear()
                cliente['deposito'].append(dep)

            cliente['saldo'] += dep
            clientes.insert(p, cliente)
            break

    with open(filename, 'w') as file:
        json.dump(clientes, file) # salva os dados atualizados

    input('Aperte ENTER para voltar...')
    menu.menu_usuario(cliente)

def saque(cliente):
    """Simula um saque na conta."""
    cpf = cliente['cpf']
    limpa_tela()
    print('SAQUE EM CONTA'.center(30))
    print('=' * 30)
    saq = float(input('Valor do saque: R$'))
    print()

    filename = 'contas/clientes'
    with open(filename) as file:
        clientes = json.load(file)

    for p, d in enumerate(clientes):
        if d['cpf'] == cpf:
            del clientes[p]

            if len(cliente['saque']) < 10:
                cliente['saque'].append(saq)
            else:
                cliente['saque'].clear()
                cliente['saque'].append(saq)

            cliente['saldo'] -= saq
            clientes.insert(p, cliente)
            break

    with open(filename, 'w') as file:
        json.dump(clientes, file) # salva os dados atualizados

def extrato(cliente):
    """Simula a listagem do extrato em banco."""
    limpa_tela()
    print('EXTRATO DA CONTA'.center(30))
    print('=' * 30)

    print()
    print('ÚLTIMOS DEPÓSITOS '.rjust(5), end='-' * 5)
    print(' ÚLTIMOS SAQUES'.rjust(10))
    print()
    for d in range(10):
        if d <= len(cliente['deposito']) - 1:
            print(f"R${cliente['deposito'][d]:.2f}".center(17), end=' ')
        if d <= len(cliente['saque']) - 1:
            print(f"R${cliente['saque'][d]:.2f}".center(25))
        else:
            print()

    input('Aperte ENTER para voltar...')
