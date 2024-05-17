import psycopg2
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo test.env
load_dotenv("test.env")

print("PG_HOST:", os.getenv('PG_HOST'))
print("PG_PORT:", os.getenv('PG_PORT'))
