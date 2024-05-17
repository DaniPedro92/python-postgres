import psycopg2
import os

password = os.getenv('PG_PASSWORD')
user = os.getenv('PG_USER')
host = os.getenv('PG_HOST_DB')
dbname = os.getenv('PG_DB')



conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port="5432"
)

cursor = conn.cursor()
cursor.execute('SELECT id, nome, cervejaria, estilo, teor_alcoolico, volume_ml, preco, quantidade_estoque, data_validade FROM cervejas;')
results = cursor.fetchall()
conn.close()

for x in results:
    print(x)


