import model_base
import sqlalchemy as sa


class Player(model_base.ModelBase):
    __tablename__ = 'players'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, index=True)
    choice = sa.Column(sa.Integer)
