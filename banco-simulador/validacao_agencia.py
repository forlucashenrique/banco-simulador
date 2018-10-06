import entrar
import menu
from limpa_tela import limpa_tela
def valida_agencia(cliente_agencia):
    ag = cliente_agencia
    while ag != '2213-1':
        limpa_tela()
        menu.menu_entrar()
        print('\tAgência incorreta. Tente novamente!')
        ag = str(input(f"{'Agência: ':>11}")).strip()

    menu.menu_entrar(ag)
    entrar.entrar_conta(ag)
