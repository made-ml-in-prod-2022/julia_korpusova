import pandas as pd
import requests
import logging
from _pytest import pathlib

logger = logging.getLogger(__name__)


def main():
    test_file = "data/test.csv"
    path = pathlib.Path(__file__).parent.parent.joinpath(test_file)
    url = "http://0.0.0.0:8000/predict/"

    data = pd.read_csv("data/test.csv").drop(columns="Unnamed: 0")
    logger.info(f"load data: shape - {data.shape}")

    features = list(data.columns)
    logger.info(f"data features: {features}")

    for row in data.itertuples():
        data_request = [x for x in row]
        request = {"data": [data_request[-13:]], "features": features}
        logger.info(f"request {request}")
        response = requests.get(url,
                                json=request,
                                )
        print(f"code: {response.status_code}, json: {response.json()}")


if __name__ == "__main__":
    main()
