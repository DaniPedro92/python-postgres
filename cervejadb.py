import psycopg2
import os

password = os.getenv('PG_PASSWORD')
user = os.getenv('PG_USER')
host_db = os.getenv('PG_HOST_DB')
database = os.getenv('PG_DB')

if not all([password, user, host_db, database]):
    raise ValueError("Erros vários! Verifique as envirtments")

try:
    conn = psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host_db,
        port="5432"
    )

    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, cervejaria, estilo, teor_alcoolico, volume_ml, preco, quantidade_estoque, data_validade FROM cervejas;')
    results = cursor.fetchall()
    conn.close()

    for x in results:
        print(x)
except psycopg2.OperationalError as e:
    print(f"OperationalError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")



