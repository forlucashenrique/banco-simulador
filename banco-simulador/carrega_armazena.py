import json

def carrega_armazena():
    """Carrega o arquivo clientes.json para a funcao armazena_dados."""

    try:
        filename = 'contas/clientes'
        with open(filename) as file:
            listagem_de_clientes = json.load(file)
    except FileNotFoundError:
        pass

    return listagem_de_clientes, filename
