class Player:
    def __init__(self,):
        self.money = 1500


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player: Player):
        if len(self.players) < 4:
            self.players.append(player)
