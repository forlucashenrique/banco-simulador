from limpa_tela import limpa_tela
from carrega_clientes import carrega
from time import sleep
import validacao_conta
import validacao_senha
import validacao_agencia
import menu

def entrar_agencia():
    limpa_tela()
    """Pede a agência do cliente."""
    menu.menu_entrar()
    agencia = str(input(f"{'Agência: ':>11}")).strip()
    validacao_agencia.valida_agencia(agencia)

def entrar_conta(minha_agencia):
    """Pede a conta do cliente."""

    conta = str(input(f"{'Conta: ':>11}")).strip()
    validacao_conta.valida_conta(conta, minha_agencia)


def entrar_senha(minha_conta, minha_agencia):
    """Pede a senha do cliente."""

    senha = str(input(f"{'Senha: ':>11}")).strip()

    validacao_senha.valida_senha(minha_conta, minha_agencia, senha)
