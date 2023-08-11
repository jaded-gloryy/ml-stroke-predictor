from os import environ
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "DATA_FILEPATH": environ["DATA_FILEPATH"],
    "CHILD_BMI": environ["CHILD_BMI"],
    "NOT_DOC": environ["NOT_DOC"]
}