import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "chave-super-secreta"
    SQLALCHEMY_DATABASE_URI = "sqlite:///meu_banco.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False