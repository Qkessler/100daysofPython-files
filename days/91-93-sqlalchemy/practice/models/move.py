from datetime import datetime
from model_base import ModelBase


class Move(ModelBase):
    def __init__(self):
        self.created = datetime.now()
        self.roll_id = None
        self.game_id = None
        self.roll_number = None
        self.player_id = None
        self.is_winning_play = False
