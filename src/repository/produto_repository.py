from repository.oracle import get_connection

TIPO_PRODUTO = {
    "Insumos": 1,
    "Fertilizantes": 2,
    "Pesticidas": 3
}

def criar(produto):
    query = """
    INSERT INTO produto (nome, id_tipo)
    VALUES (:nome, :id_tipo)
    """
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, produto)
            connection.commit()
    except Exception as e:
        print(e)


def ler(produto_id):
    query = "SELECT * FROM produto WHERE id = :id"
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, id=produto_id)
                resultado = cursor.fetchone()
                if resultado:
                    return {
                        "id": resultado[0],
                        "id_tipo": resultado[1],
                        "nome": resultado[2]
                    }
                return None
    except Exception as e:
        print(e)


def atualizar(produto):
    query = """
    UPDATE produto
    SET nome = :nome, id_tipo = :id_tipo
    WHERE id = :id
    """
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, produto)
            connection.commit()
    except Exception as e:
        print(e)


def deletar(produto_id):
    query = "DELETE FROM produto WHERE id = :id"
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, id=produto_id)
            connection.commit()
    except Exception as e:
        print(e)


def listar_todos(id_tipo: int):
    query = """
    SELECT p.id, t.nome as tipo, p.nome 
    FROM produto p inner join tipo_produto t on p.id_tipo = t.id
    WHERE p.id_tipo = :id_tipo
    ORDER BY p.id
    """
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, id_tipo=id_tipo)
                resultados = cursor.fetchall()
                return resultados
    except Exception as e:
        print(e)
