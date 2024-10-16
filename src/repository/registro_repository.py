from repository.oracle import get_connection

def criar(registro):
    query = """
    INSERT INTO registro_produto (id_produto, estoque, data)
    VALUES (:id_produto, :estoque, SYSDATE)
    """
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, registro)
            connection.commit()
    except Exception as e: 
        print(e)


def ler(id_produto):
    query = """
    SELECT p.id, p.nome, t.nome as tipo, sum(r.estoque)
    FROM registro_produto r
    INNER JOIN produto p on r.id_produto = p.id
    INNER JOIN tipo_produto t on p.id_tipo = t.id
    WHERE p.id = :id_produto
    GROUP BY p.id, p.nome, t.nome
    """

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, id_produto=id_produto)
                resultado = cursor.fetchone()
                if resultado:
                    return {
                        "id_produto": resultado[0],
                        "nome": resultado[1],
                        "tipo": resultado[2],
                        "estoque": resultado[3]
                    }
                return None
    except Exception as e:
        print(e)


def atualizar(registro):
    query = """
    UPDATE registro_produto
    SET estoque = :estoque
    WHERE id = :id
    """
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, registro)
            connection.commit()
    except Exception as e:
        print(e)

def listar_todos():
    query = """
    SELECT p.id, p.nome, t.nome as tipo, sum(r.estoque)
    FROM registro_produto r
    INNER JOIN produto p on r.id_produto = p.id
    INNER JOIN tipo_produto t on p.id_tipo = t.id
    GROUP BY p.id, p.nome, t.nome
    """
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    except Exception as e:
        print(e)

def listar_consumos():
    query = """
    SELECT p.id, p.nome, t.nome as tipo, ABS(r.estoque), r.data
    FROM registro_produto r
    INNER JOIN produto p on r.id_produto = p.id
    INNER JOIN tipo_produto t on p.id_tipo = t.id
    WHERE r.estoque < 0
    """
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    except Exception as e:
        print(e)

def listar_consumos_por_por_dia():
    query = """
    SELECT t.nome as tipo, abs(sum(r.estoque)) as total_consumo, TRUNC(data) as data
    FROM registro_produto r
    INNER JOIN produto p on r.id_produto = p.id
    INNER JOIN tipo_produto t on p.id_tipo = t.id
    WHERE r.estoque < 0
    GROUP BY t.nome, TRUNC(data)
    """
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    except Exception as e:
        print(e)






