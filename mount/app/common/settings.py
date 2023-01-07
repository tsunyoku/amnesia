import os

from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = int(os.environ["LOG_LEVEL"])

DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = int(os.environ["DB_PORT"])
DB_NAME = os.environ["DB_NAME"]

REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PORT = int(os.environ["REDIS_PORT"])

GEOLOCATION_DB_PATH = os.environ["GEOLOCATION_DB_PATH"]
