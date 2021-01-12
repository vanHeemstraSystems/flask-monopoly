from typing import Union, List
from copy import deepcopy
from app.game.game import *

Field = Union[CityField, PowerplantField, SurpriseField, FineField, TrainField, PlaceholderField]


def ai_move(g: Game):
    move = {
        'buy': None,
        'build': None
    }
    current_player: Player = g.players[g.current_player_index]
    current_field: Field = g.board[current_player.current_field_id]
    current_money: int = current_player.money
    owned_fields: List[Field] = deepcopy(current_player.owned_fields)
    build_count = 0

    if g.can_buy and current_money > current_field.price:
        move['buy'] = True
        current_money -= current_field.price

    owned_city_fields = [field for field in owned_fields if isinstance(field, CityField)]
    sorted_owned_city_fields: List[CityField] = sorted(owned_city_fields, key=lambda f: f.build_price, reverse=True)
    for field in sorted_owned_city_fields:
        if field.build_price < current_money and build_count < 3 and field.build != 'h':
            while field.build != 'h' and build_count < 3 and field.build_price < current_money:
                build_count += 1
                current_money -= field.build_price
                move['build'] += '{};'.format(field.id)
        if build_count == 3:
            break

    return move
