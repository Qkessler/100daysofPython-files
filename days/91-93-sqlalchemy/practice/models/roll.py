from model_base import ModelBase
import sqlalchemy
from datetime import datetime


class Roll(ModelBase):
    __tablename__ = 'rolls'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True)
    created = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
    def __init__(self, name: str):
        self.name = name
