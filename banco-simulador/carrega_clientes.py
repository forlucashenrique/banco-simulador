import json

def carrega():
    """Carrega o arquivo clientes.json para ser manipulado pelo programa."""
    try:
        filename = 'contas/clientes'
        with open(filename) as file:
            listagem_de_clientes = json.load(file)
    except FileNotFoundError:
        pass

    return listagem_de_clientes
