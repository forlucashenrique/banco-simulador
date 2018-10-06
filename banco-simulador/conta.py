import json
from random import randint
from limpa_tela import limpa_tela
from carrega_clientes import carrega
from carrega_armazena import carrega_armazena

def cadastro():
    """Cria um dicionário com os dados do usuário."""

    print('CADASTRO'.center(30))
    print('=' * 30)
    dados_usuario = dict()
    dados_usuario['nome'] = str(input(f"{'Nome: ':>11}")).strip().title()
    dados_usuario['cpf'] = str(input(f"{'CPF: ':>11}")).strip()
    dados_usuario['telefone:'] = str(input(f"{'Telefone: ':>11}")).strip()
    dados_usuario['senha'] = str(input(f"{'Senha: ':>11}")).strip()
    while len(dados_usuario['senha']) < 6 or len(dados_usuario['senha']) > 6:
        print(f"{'A senha precisa ter 6 dígitos.':>40}")
        dados_usuario['senha'] = str(input(f"{'Senha: ':>11}")).strip()
    dados_usuario['deposito'] = []
    dados_usuario['saque'] = []
    dados_usuario['saldo'] = 0.0

    print()

    agencia_conta_cadastro(dados_usuario) # chama a funcao agencia_conta para armazanar a agencia e a conta do cliente no dicionario.

    print(f"{'Agência:':>10} {dados_usuario['agencia']}")
    print(f"{'Conta:':>10} {dados_usuario['conta']}")

    armazena_dados(dados_usuario.copy()) # chama a funcao armazena_dados para armazenar os dados completos do cliente.

    print('=' * 30)
    print('CONTA CRIADA COM SUCESSO!'.center(30))
    print()
    input('Aperte ENTER para continuar...')



def armazena_dados(dicionario):
    """Armazana os dados do usuário em um arquivo json e o salva no diretório 'contas'."""
    clientes, filename = carrega_armazena()
    clientes.append(dicionario)
    with open(filename,'w') as file:
        json.dump(clientes, file)


def agencia_conta_cadastro(dicionario):
    agencia = '2213-1'
    conta = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}-{randint(0, 9)}'
    dicionario['agencia'] = agencia
    dicionario['conta'] = conta
