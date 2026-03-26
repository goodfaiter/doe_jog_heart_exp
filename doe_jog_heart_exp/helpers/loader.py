import pandas as pd


def load_data() -> pd.DataFrame:
    data = {
        "experiment": [1, 2, 3, 4, 5, 6, 7, 8],
        "type": ["Walking", "Walking", "Walking", "Walking", "Running", "Running", "Running", "Running"],
        "weight": ["0 kg", "0 kg", "5 kg", "5 kg", "0 kg", "0 kg", "5 kg", "5 kg"],
        "frequency": ["2 / week", "5 / week", "2 / week", "5 / week", "2 / week", "5 / week", "2 / week", "5 / week"],
        "distance": ["2 km", "5 km", "5 km", "2 km", "5 km", "2 km", "2 km", "5 km"],
        "before_bmp": [155, 162, 153, 146, 154, 168, 171, 165],
        "after_bmp": [161, 143, 145, 133, 145, 154, 168, 150],
        "before_rpe": [3, 7, 6, 3, 3, 5, 6, 5],
        "after_rpe": [3, 6, 5, 3, 4, 2.5, 4, 2],
        "questionnaire_q1": [3, 4, 3, 2, 7, 5, 6, 8],
        "questionnaire_q2": [2, 7, 3, 2, 9, 7.5, 8, 3],
        "questionnaire_q3": [3, 4, 3.5, 7, 8, 7, 7, 8],
    }

    df = pd.DataFrame(data)
    return df
