from limpa_tela import limpa_tela
import operacoes_banco
from barra_progresso import barra_progresso


def menu_banco():

    """Simula o menu do banco."""

    print('SIMULADOR BANCÁRIO'.center(30))
    print('=' * 30)
    print(f"""
    {'ENTRAR':<15}[1]
    {'CRIAR CONTA':<15}[2]
    {'SAIR':<15}[3]\n""")

    opcao = int(input(f"{'Opção: ':>11}"))

    return opcao

def menu_entrar(agencia_cliente='', conta_cliente='', senha_cliente=''):
    limpa_tela()
    print('ACESSAR CONTA'.center(30))
    print('=' * 30)
    if agencia_cliente:
        print(f"{'Agência: ':>11}{agencia_cliente}")
    if conta_cliente:
        print(f"{'Conta: ':>11}{conta_cliente}")
    if senha_cliente:
        print(f"{'Senha: ':>11}{senha_cliente}\n")

def menu_usuario(info_user):
    """Mostra o menu do usário simulando um caixa eletrônico com as opções disponíveis."""

    dados_user = info_user

    while True:
        limpa_tela()

        print(f"BEM-VINDO {dados_user['nome']}".center(30))
        print('=' * 30)

        print(f"""
    {'SALDO':<15}[1]
    {'DEPOSITO':<15}[2]
    {'SAQUE':<15}[3]
    {'EXTRATO':<15}[4]
    {'SAIR':<15}[5]
    \n""")
        escolha = int(input(f"{'Opção: ':>11} "))

        if escolha == 1:
            operacoes_banco.saldo(dados_user)
        elif escolha == 2:
            operacoes_banco.deposito(dados_user)
        elif escolha == 3:
            operacoes_banco.saque(dados_user)
        elif escolha == 4:
            operacoes_banco.extrato(dados_user)
        elif escolha == 5:
            print()
            print('<< VOLTE SEMPRE! >>')
            barra_progresso()
            break

    limpa_tela()
