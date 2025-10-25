
# def create_player(name, xp, team):
#     return{
#        "name": name,
#         "XP": xp,
#         "team": team 
#     }

# def introduce_player(player):
#     name = player["name"]
#     team = player["team"]
#     print(f"Hello! My name is {name} and I play for {team}")

# nico = create_player("Nico", 1500, "Team X")
# lynn = create_player("Lynn", 1500, "Team Y")

# introduce_player(nico)
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed  

class GuardDog(Dog):

    def __init__(self, name, breed):
        super().__init__(
            name,
            5,
            breed
        )
        self.agressive = True
    
    def rrrr(self):
        print("stay away")

class Puppy(Dog):
    
    def __init__(self, name, breed):
        super().__init__(
            name,
            0.1,
            breed
        )

    # def __str__(self):
    #     return f"Puppy named {self.name}, breed: {self.breed}"
    
    def woof_woof(self):
        print("Woof Woof")
    
    def introduce(self):
        self.woof_woof()
        print(f"My name is {self.name}")
        self.woof_woof() 

ruffus = Puppy("Ruffus", "Beagle")
bibi = GuardDog("Bibi", "Dalmatian")

ruffus.woof_woof()
bibi.rrrr()