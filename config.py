from dotenv import load_dotenv
from os import getenv

from urllib.parse import quote_plus


load_dotenv()

user = getenv('DATABASE_USER')
password = getenv('DATABASE_PASSWORD')
host = getenv('DATABASE_HOST')
name = getenv('DATABASE_NAME')


class Config:
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{quote_plus(password)}@{host}/{name}?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = getenv('SECRET_KEY')
