import psycopg2
import os
from sqlalchemy import create_engine
from create_tables_sql import commands

HOST_DB = os.getenv('HOST_DB')
PORT_DB = os.getenv('PORT_DB')
USER_DB = os.getenv('USER_DB')
PASSWORD_DB = os.getenv('PASSWORD_DB')
NAME_DB = os.getenv('NAME_DB')

# print(HOST_DB, PORT_DB, USER_DB, PASSWORD_DB, NAME_DB)
conn = psycopg2.connect(dbname=NAME_DB, user=USER_DB, password=PASSWORD_DB, host=HOST_DB, port=PORT_DB)
conn.autocommit = True
engine = create_engine(f'postgresql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{NAME_DB}')
with conn.cursor() as cur:
    for command in commands:
        cur.execute(command)

cur.close()
conn.close()
