import psycopg2
import os

# Obtenha as informações de conexão do ambiente
host = os.getenv('PG_HOST')
port = os.getenv('PG_PORT')
database = os.getenv('PG_DATABASE')
user = os.getenv('PG_USER')
password = os.getenv('PG_PASSWORD')

try:
    # Conecte-se ao banco de dados usando as informações do ambiente
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    cursor = conn.cursor()
    query = "SELECT * FROM public.contacts"
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Erro ao conectar ao PostgreSQL: {e}")




