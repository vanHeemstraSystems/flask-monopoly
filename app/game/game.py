from random import randint
from app.game.fields import *


class PlaceholderField:
    def __init__(self, data):
        self.id = data['id']
        self.label = data['label']


class CityField:
    def __init__(self, data):
        self.id = data['id']
        self.label = data['label']
        # price = data.price

    def on_enter(self):
        pass


class Player:
    def __init__(self):
        self.money = 3000
        self.current_field = 0

    def move(self, steps: int):
        pass


class Game:
    def __init__(self, players_count: int):
        self.players = []
        self.current_player = 0
        self.board = []

        for _ in range(players_count):
            self.players.append(Player())

        self._render_board()

    def next_turn(self):
        self._next_player()
        move = randint(2, 12)

    def _next_player(self):
        if self.current_player + 1 == len(self.players):
            self.current_player = 0
        else:
            self.current_player += 1

    def _render_board(self):
        for field in FIELDS:
            if field['type'] == CITY:
                f = CityField(field)
            else:
                f = PlaceholderField(field)

            self.board.append(f)
