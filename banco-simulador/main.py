import conta
import menu
from time import sleep
from limpa_tela import limpa_tela
from entrar import entrar_agencia
from barra_progresso import barra_progresso


while True:
    op = menu.menu_banco()
    if op == 1:
        barra_progresso()
        entrar_agencia()
    elif op == 2:
        limpa_tela()
        conta.cadastro()
        limpa_tela()
    elif op == 3:
        break


print()
print('=' * 30)
print('Finalizando o simulador...')
sleep(2)
print('<< PROGRAMA ENCERRADO! >>')
