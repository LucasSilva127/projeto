import psycopg2

def conectardb():
    con = psycopg2.connect(
        host='localhost',
        database='bancodedados',
        user='postgres',
        password='12345'
    )
    return con