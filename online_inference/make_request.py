import numpy as np
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
    print(data.head())

    features = data.columns.to_list()
    print(features)

    for row in data.itertuples():
        data_request = [x for x in row]
        request = {"data": [data_request], "features": features}
        print(request)
        response = requests.get(url,
                                json=request,
                                )
        logging.info(f"code: {response.status_code}, json: {response.json()}")


if __name__ == "__main__":
    main()
