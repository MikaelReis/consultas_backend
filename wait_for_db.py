import time
import psycopg2
from psycopg2 import OperationalError

print("Aguardando o banco de dados...")

while True:
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="db",
            port="5432",
        )
        conn.close()
        print("Banco de dados disponível!")
        break
    except OperationalError:
        print("Banco de dados não disponível ainda. Tentando novamente...")
        time.sleep(1)
