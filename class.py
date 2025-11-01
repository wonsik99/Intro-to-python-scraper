class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello! I'm {self.name} and I paly for {self.team}")

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.players = []

    def show_players(self):
        for player in self.players:
            player.introduce()

    def add_player(self, name):
        new_player = Player(name, self.name)
        self.players.append(new_player)

    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(name)



    def total_xp(self):
        xps = 0
        for player in self.players:
            xps += player.xp

        print(xps) 

# nico = Player(
#     name = "nico",
#     team = "Team X"
# )

# lynn = Player(
#     name = "lynn",
#     team = "Team Y"
# )

team_x = Team("Team X")
team_x.add_player("nico")

team_blue = Team("Team Blue")
team_blue.add_player("lynn")

team_blue.show_players()
