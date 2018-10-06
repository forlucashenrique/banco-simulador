import menu
from carrega_clientes import carrega
import entrar
from limpa_tela import limpa_tela


def valida_conta(cliente_conta, cliente_agencia):
    cnt = cliente_conta
    ag = cliente_agencia

    dados_clientes = carrega()

    lista_contas = []
    for dado in dados_clientes:
        lista_contas.append(dado['conta'])

    while cnt not in lista_contas:
        limpa_tela()
        menu.menu_entrar(ag)
        print('\tConta inexistente. Tente novamente!')
        cnt = str(input(f"{'Conta: ':>11}")).strip()
        
    menu.menu_entrar(ag, cnt)
    entrar.entrar_senha(cnt, ag)
