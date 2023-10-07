import pandas as pd


def preprocess(data_json: dict, features: list) -> pd.DataFrame:
    """
    The function preprocess takes a JSON object and a list of features, and returns a pandas DataFrame
    with the selected features.
    
    :param data_json: The `data_json` parameter is a dictionary that contains the data in JSON format.
    It is assumed to have the following structure:
    :param features: The `features` parameter is a list of column names that you want to include in the
    resulting DataFrame
    :return: a pandas DataFrame object.
    """
    data = pd.DataFrame(
        {
            "Avg. Area Income": data_json.features["avg_area_income"],
            "Avg. Area House Age": data_json.features["avg_area_house_age"],
            "Avg. Area Number of Rooms": data_json.features["avg_area_number_of_rooms"],
            "Avg. Area Number of Bedrooms": data_json.features[
                "avg_area_number_of_bedrooms"
            ],
            "Area Population": data_json.features["area_population"],
            "Address": data_json.features["address"],
        },
        index=[0],
    )

    data = data[features]
    data.columns = ["feat_" + str(col) for col in data.columns]

    return data
