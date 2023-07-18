from os import environ
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "DATA_FILEPATH": environ["DATA_FILEPATH"],
    # "": environ[""]
}