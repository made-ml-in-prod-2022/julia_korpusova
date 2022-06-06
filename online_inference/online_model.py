import os
import logging
import pathlib
from typing import List, Union, Optional
import pandas as pd
import pickle
import uvicorn
import gdown

from fastapi import FastAPI
from pydantic import BaseModel, conlist
from sklearn.pipeline import Pipeline

DEFAULT_MODEL_URL = "https://drive.google.com/file/d/1D9I5kaPQIhiiHwEQACpELTGBF61oqg3a/view?usp=sharing"

logger = logging.getLogger(__name__)

app = FastAPI()
model: Optional[Pipeline] = None


class Request(BaseModel):
    data: List[conlist(Union[float, str, int, None], min_items=13, max_items=13)]
    features: List[str]


class Prediction(BaseModel):
    condition: int


def load_model(path: str) -> Pipeline:
    with open(path, "rb") as file:
        return pickle.load(file)


@app.get("/")
def main():
    return "App for predictions heart diseases <3"


@app.on_event("startup")
def startup():
    global model
    model_local_path = "models/model.pkl"
    model_path = pathlib.Path(__file__).parent.joinpath(model_local_path)
    print(model_path)
    print(model_path.exists())
    if not model_path.exists():
        model_url = os.getenv("MODEL_URL")
        if model_url is None:
            model_url = DEFAULT_MODEL_URL
            logger.info("loading model from Google-Drive")
        gdown.download(model_url, model_local_path, fuzzy=True)

    model = load_model(str(model_path))
    logger.info("model upload")


@app.get("/health")
def health() -> int:
    return not (model is None)


@app.get("/predict/", response_model=List[Prediction])
def predict(request: Request):
    data = pd.DataFrame(request.data, columns=request.features)
    predictions = model.predict(data)
    return [Prediction(label=int(lbl))
            for lbl in predictions
            ]


if __name__ == "__main__":
    uvicorn.run("online_model:app", host="0.0.0.0",
                port=os.getenv("PORT", 8000))

