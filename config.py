import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI =(f'postgresql://{os.getenv("POSTGRES_USER")}:'
                             f'{os.getenv("POSTGRES_PASSWORD")}@db:5432/{os.getenv("POSTGRES_DB")}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
