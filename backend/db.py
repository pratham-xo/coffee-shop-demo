import os

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def get_database_url():
    return os.getenv(
        "DATABASE_URL",
        "postgresql://coffee:coffee123@localhost:5432/coffeedb"
    )
