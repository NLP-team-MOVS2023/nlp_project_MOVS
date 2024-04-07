import psycopg2
from sqlalchemy import create_engine
from create_tables_sql import commands

HOST_DB = 'dpg-cnvsglmd3nmc73f5mi3g-a.frankfurt-postgres.render.com'
PORT_DB = 5432
USER_DB = 'nlp_project_gmuh_user'
PASSWORD_DB = 'nYVFTFlSYHF6DL1dLhLH19aDNIDtpR0e'
NAME_DB = 'nlp_project_gmuh'

# print(HOST_DB, PORT_DB, USER_DB, PASSWORD_DB, NAME_DB)
conn = psycopg2.connect(dbname=NAME_DB, user=USER_DB, password=PASSWORD_DB, host=HOST_DB, port=PORT_DB)
conn.autocommit = True
engine = create_engine(f'postgresql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{NAME_DB}')
with conn.cursor() as cur:
    for command in commands:
        cur.execute(command)

cur.close()
conn.close()
