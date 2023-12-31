from fastapi import FastAPI
from pydantic import BaseModel
import json
import joblib

from src import utils

app = FastAPI()

model = joblib.load("src/model_artifacts/model.joblib")
config = json.load(open("src/model_artifacts/config.json"))
features = config["features"]


class Request(BaseModel):
    features: dict
    provider: str


class Response(BaseModel):
    features: dict
    output: float
    provider: str


@app.get("/status")
async def status():
    return {"status": "OK"}


@app.post("/predict")
async def predict(data_json: Request):
    """
    This function takes in a JSON request containing data, preprocesses the data using a utility
    function, makes predictions using a pre-trained model, and returns a JSON response containing the
    predicted output.

    :param data_json: The `data_json` parameter is the JSON data received in the Pydantic Request body. It
    contains the input data for making predictions

    :return: The code is returning a Response object with the following attributes:
    - features: the features from the data_json object
    - output: the predictions generated by the model
    - provider: the provider from the data_json object
    """
    processed_data = utils.preprocess(data_json, features)
    predictions = model.predict(processed_data)

    return Response(
        features=data_json.features,
        output=predictions[0],
        provider=data_json.provider,
    )
