import os

# Obtém o valor da variável de ambiente PG_PASSWORD
pg_password = os.getenv('PG_PASSWORD')

# Verifica se a variável de ambiente foi definida
if pg_password is not None:
    print("Valor da variável de ambiente PG_PASSWORD:", pg_password)
else:
    print("A variável de ambiente PG_PASSWORD não está definida.")