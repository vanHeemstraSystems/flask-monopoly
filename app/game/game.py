class Player:
    def __init__(self, player_id):
        self.money = 1500
        self.id = id


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player: Player):
        if len(self.players) < 4:
            self.players.append(player)
