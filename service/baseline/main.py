from fastapi import FastAPI, HTTPException, Response
from schemas import ObjectSubject, PredictProba
import joblib

app = FastAPI()

@app.get('/')
def root__get():
    return {"message": "Hello World"}

@app.post('/predict_proba',
         response_model=PredictProba,
         summary='Predict Proba')

def predict_proba(vals: ObjectSubject):
    # pipeline = joblib.load('')
    return {'value':4.5}
