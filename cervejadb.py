import psycopg2

conn = psycopg2.connect(
    dbname="db-fdp",
    user="postgres",
    password="Abcd1234!",
    host="database-ea.cvkei0o2ei4o.eu-central-1.rds.amazonaws.com",
    port="5432"
)

cursor = conn.cursor()
cursor.execute('SELECT id, nome, cervejaria, estilo, teor_alcoolico, volume_ml, preco, quantidade_estoque, data_validade FROM cervejas;')
results = cursor.fetchall()
conn.close()

for x in results:
    print(x)
