from fastapi import FastAPI
from schemas import ObjectSubject
from ML.pipeline import predict_pipeline

app = FastAPI()


@app.get('/')
def root_get():
    return {"message": "Hello World"}


@app.post('/predict', summary='Predict')
def predict(vals: ObjectSubject):
    """Uploads samples and returns predictions as Json"""
    dict_vals = dict(vals)
    return predict_pipeline(dict_vals)
