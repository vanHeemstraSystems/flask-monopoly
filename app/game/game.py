from typing import Union
from random import randint
from app.game.fields import *


class Player:
    def __init__(self, pid: int):
        self.money = 3000
        self.current_field_id = 0
        self.id = pid
        self.owned_fields = []

    def move(self, steps: int):
        if self.current_field_id + steps > 39:
            self.current_field_id = self.current_field_id - len(FIELDS) - 1 + steps
        else:
            self.current_field_id += steps


class PlaceholderField:
    def __init__(self, data):
        self.id = data['id']
        self.label = data['label']
        self.type = data['type']

    def on_enter(self, player: Player):
        return 'field {} has been stepped on by player {}'.format(self.id, player.id)


class CityField:
    def __init__(self, data):
        self.id = data['id']
        self.type = data['type']
        self.label = data['label']
        self.price = data['price']
        self.build_price = data['build_price']
        self.pricing = data['pricing']
        self.owner = None

    def on_enter(self, player: Player):
        return 'field {} has been stepped on by player {}'.format(self.id, player.id)


class Game:
    def __init__(self, players_count: int):
        self.players = []
        self.current_player_index = 0
        self.board = []
        self.msgs = []
        self.can_buy = False

        for i, _ in enumerate(range(players_count)):
            self.players.append(Player(i))

        self._render_board()

    def next_turn(self, payload):
        if payload['buy']:
            self._sell_field(self.players[self.current_player_index],
                             self.board[self.players[self.current_player_index].current_field_id])
        self._next_player()
        move = randint(2, 12)
        player = self.players[self.current_player_index]
        player.move(move)
        msg = self.board[player.current_field_id].on_enter(player)
        if self.board[player.current_field_id].type in [CITY] and not self.board[
            player.current_field_id].owner and player.money > self.board[player.current_field_id].price:
            self.can_buy = True
        self._add_message(msg)

    def _sell_field(self, player: Player, field: Union[CityField]):
        player.money -= field.price
        player.owned_fields.append(field)
        field.owner = player
        print(player.money, player.owned_fields, field.owner)

    def _add_message(self, msg):
        self.msgs.append(msg)

    def _next_player(self):
        if self.current_player_index + 1 == len(self.players):
            self.current_player_index = 0
        else:
            self.current_player_index += 1
        self.can_buy = False

    def _render_board(self):
        for field in FIELDS:
            if field['type'] == CITY:
                f = CityField(field)
            else:
                f = PlaceholderField(field)

            self.board.append(f)
