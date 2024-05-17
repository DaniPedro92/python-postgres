import psycopg2
from dotenv import load_dotenv
import os
from tabulate import tabulate
from colorama import Fore, Style

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

    table_data = [list(row) for row in results]
    column_names = [desc[0] for desc in cursor.description]

    columm_color = {
        'id': Fore.GREEN,
        'nome': Fore.GREEN,
        'cervejaria': Fore.GREEN,
        'estilo': Fore.GREEN,
        'teor_alcoolico': Fore.GREEN,
        'volume_ml': Fore.GREEN,
        'preco': Fore.GREEN,
        'quantidade_estoque': Fore.GREEN,
        'data_validade': Fore.GREEN
    }


    colored_column_names = [columm_color.get(column_name.lower(), '') + column_name + Style.RESET_ALL for column_name in column_names]
    print(tabulate(table_data, headers=colored_column_names, tablefmt="grid"))

except psycopg2.Error as e:
    print(f"Erro ao conectar ao PostgreSQL: {e}")

