from carrega_clientes import carrega
from limpa_tela import limpa_tela
import menu
from time import sleep
from barra_progresso import barra_progresso

def valida_senha(cliente_conta,cliente_agencia, cliente_senha):
    cnt = cliente_conta
    ag = cliente_agencia
    snh = cliente_senha

    dados_clientes = carrega()

    for dado in dados_clientes:
        if cnt == dado['conta']:
            while snh != dado['senha']:
                limpa_tela()
                menu.menu_entrar(ag, cnt)
                print('\tSenha incorreta.')
                snh = str(input(f"{'Senha: ':>11}")).strip()

            usuario = dado
    menu.menu_entrar(ag, cnt, snh)
    print()
    barra_progresso()
    return menu.menu_usuario(usuario)
