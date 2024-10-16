import pandas as pd
from repository import produto_repository


def criar_produto(tipo_produto):
    print("=" * 50)
    print(f"Cadastrando {tipo_produto}")
    print("=" * 50)
    nome = input("Informe o nome do produto: ")

    produto = {
        "nome": nome,
        "id_tipo": produto_repository.TIPO_PRODUTO[tipo_produto]
    }
    produto_repository.criar(produto)

def listar_produto(tipo_produto):
    print("=" * 50)
    print(f"Listando {tipo_produto}")
    print("=" * 50)

    produtos = produto_repository.listar_todos(produto_repository.TIPO_PRODUTO[tipo_produto])

    if produtos:
        print(pd.DataFrame.from_records(produtos, columns=['Id', 'Tipo', 'Nome'], index='Id'))
    else:
        print(f"Não existe {tipo_produto} cadastrados")

def excluir_produto(tipo_produto):
    print("=" * 50)
    print(f"Excluindo {tipo_produto}")
    print("=" * 50)

    try:
        id_produto = int(input("Informe o id do produto que deseja excluir: "))
        produto = produto_repository.ler(id_produto)
        if produto:
            produto_repository.deletar(id_produto)
            print("Produto excluído com sucesso!!!")
        else:
            print("Produto não encontrado!!!")
    except ValueError:
        print("Id do produto inválido, informe um número")
    else:
        listar_produto(tipo_produto)

