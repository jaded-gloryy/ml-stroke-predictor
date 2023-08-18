from os import environ
from dotenv import load_dotenv

load_dotenv()

try:
    CONFIG = {
        "DATA_FILEPATH": environ["DATA_FILEPATH"],
        "CHILD_BMI": environ["CHILD_BMI"],
        "NOT_DOC": environ["NOT_DOC"]
    }
except KeyError:
    CONFIG = {
        "DATA_FILEPATH": "data/healthcare-dataset-stroke-data.csv",
        "CHILD_BMI": "data/bmiagerev.csv",
        "NOT_DOC": "data/notdoc.png"
    }