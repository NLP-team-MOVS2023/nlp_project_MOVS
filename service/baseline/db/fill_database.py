import psycopg2
from config_reader import config
from sqlalchemy import create_engine
from create_tables_sql import commands

HOST_DB = config.HOST_DB.get_secret_value()
PORT_DB = config.PORT_DB.get_secret_value()
USER_DB = config.USER_DB.get_secret_value()
PASSWORD_DB = config.PASSWORD_DB.get_secret_value()
NAME_DB = config.NAME_DB.get_secret_value()

# print(HOST_DB, PORT_DB, USER_DB, PASSWORD_DB, NAME_DB)
conn = psycopg2.connect(dbname=NAME_DB, user=USER_DB, password=PASSWORD_DB, host=HOST_DB, port=PORT_DB)
engine = create_engine(f'postgresql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{NAME_DB}')
with conn.cursor() as cur:
    for command in commands:
        cur.execute(command)
cur.close()
conn.close()
