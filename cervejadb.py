import psycopg2
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo test.env
load_dotenv("test.env")

try:
    conn = psycopg2.connect(
        dbname=os.getenv('PG_DATABASE'),
        user=os.getenv('PG_USER'),
        password=os.getenv('PG_PASSWORD'),
        host=os.getenv('PG_HOST'),
        port=os.getenv('PG_PORT')
    )

    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, cervejaria, estilo, teor_alcoolico, volume_ml, preco, quantidade_estoque, data_validade FROM cervejas;')
    results = cursor.fetchall()
    conn.close()

    for x in results:
        print(x)
except psycopg2.Error as e:
    print(f"Erro ao conectar ao PostgreSQL: {e}")
