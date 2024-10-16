import oracledb

def get_connection():
    return oracledb.connect(
        user='rm559935', password="170688", dsn='oracle.fiap.com.br:1521/ORCL')
