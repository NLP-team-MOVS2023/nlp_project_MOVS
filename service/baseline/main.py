from fastapi import FastAPI, HTTPException
from schemas import ObjectSubject
from ML.pipeline import predict_pipeline
from service.baseline.db.config_reader import config
import os
import psycopg2
import pandas as pd
import datetime
import time

try:
    HOST_DB = config.HOST_DB.get_secret_value()
    PORT_DB = config.PORT_DB.get_secret_value()
    USER_DB = config.USER_DB.get_secret_value()
    PASSWORD_DB = config.PASSWORD_DB.get_secret_value()
    NAME_DB = config.NAME_DB.get_secret_value()
except:
    HOST_DB = os.getenv('HOST_DB')
    PORT_DB = os.getenv('PORT_DB')
    USER_DB = os.getenv('USER_DB')
    PASSWORD_DB = os.getenv('PASSWORD_DB')
    NAME_DB = os.getenv('NAME_DB')

app = FastAPI()


@app.get('/')
def root_get():
    return {"message": "Добро пожаловать на сервис для проекта"}


@app.get('/ping')
def ping_get():
    return {"message": "OK"}


@app.post('/predict', summary='Predict')
def predict(vals: ObjectSubject, user):
    """Uploads samples and returns predictions as Json"""

    try:
        conn = psycopg2.connect(dbname=NAME_DB, user=USER_DB, password=PASSWORD_DB, host=HOST_DB, port=PORT_DB)
        cur = conn.cursor()
    except:
        raise HTTPException(status_code=422)

    dict_vals = dict(vals)

    cur.execute('''select max(id) from ml_model_actions;''')
    row = cur.fetchone()
    if row:
        max_id = row[0] + 1

    cur.execute(f'''select user_id from users where name = "{user}";''')
    row = cur.fetchone()
    if row:
        user_id = row[0]
    else:
        return {"message": "Создайте пользователя /create_user"}

    predicate = predict_pipeline(dict_vals)
    for i in predicate:
        cur.execute(f'''INSERT
                            INTO
                            ml_model_actions
                            VALUES({max_id}, {user_id}, {predicate[i]['subjects']}, {predicate[i]['objects']}, {predicate[i]['predicates']}, {predicate[i]['probabilities']});''')

    cur.close()
    conn.close()
    return max_id


@app.get('/get_result', summary='Result')
def get_result(res_id: int):
    try:
        conn = psycopg2.connect(dbname=NAME_DB, user=USER_DB, password=PASSWORD_DB, host=HOST_DB, port=PORT_DB)
        cur = conn.cursor()
    except:
        raise HTTPException(status_code=422)

    cur.execute(f'''select * from ml_model_actions where id = {res_id};''')
    rows = cur.fetchall()
    res = {}
    for i in enumerate(rows):
        res[i] = {'subjects': rows[2], 'objects': rows[3], 'predicates': rows[4], 'probabilities': rows[5]}

    cur.close()
    conn.close()
    return res


@app.post('/create_user')
def create_user(user: str):
    try:
        conn = psycopg2.connect(dbname=NAME_DB, user=USER_DB, password=PASSWORD_DB, host=HOST_DB, port=PORT_DB)
        cur = conn.cursor()
    except:
        raise HTTPException(status_code=422)

    try:
        base_df = pd.read_sql('select * from user_table', con=conn)
        print(base_df)
        if base_df[base_df['name'] == user.name].empty():
            cur.execute(f'''INSERT
                            INTO
                            users
                            VALUES({user.base_df.id.max() + 1}, {user.name}, {time.mktime(datetime.datetime.now().timetuple())});''')
            return {"message": "Юзер удачно добавлен"}
        else:
            return {"message": "Юзер существует"}

        cur.close()
        conn.close()
    except:
        raise HTTPException(status_code=422)
