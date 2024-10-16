import pandas as pd
from repository import registro_repository


def criar_registro_entrada():
    print("=" * 50)
    print("Criando registros de entrada no estoque")
    print("=" * 50)
    id_produto = input("Informe o id do produto: ")
    estoque = float(input("Informe a quantidade de entrada de estoque: "))

    registro = {
        "id_produto": id_produto,
        "estoque": estoque
    }
    registro_repository.criar(registro)
    print("Registro cadastrado com sucesso!!!")

def criar_registro_saida():
    print("=" * 50)
    print("Criando registros de saída estoque")
    print("=" * 50)
    id_produto = input("Informe o id do produto: ")
    estoque = float(input("Informe a quantidade de saída de estoque: "))

    registro_estoque = registro_repository.ler(id_produto)
    if not registro_estoque or registro_estoque["estoque"] < estoque:
        print("Não existe estoque suficiente para efetuar a saída!!!")
        return 

    registro = {
        "id_produto": id_produto,
        "estoque": estoque * -1
    }
    registro_repository.criar(registro)
    print("Registro cadastrado com sucesso!!!")

def listar_registro():
    print("=" * 50)
    print("Listando registros de estoque")
    print("=" * 50)

    registros = registro_repository.listar_todos();

    if registros:
        print(pd.DataFrame.from_records(registros, columns=['Id_Produto', 'Nome', 'Tipo', 'Estoque'], index='Id_Produto'))
    else:
        print("Não existe registros")
