# 3 pillars of object-oriented programming:
# 1. Inheritance: Parent-child relationship exists in classes
# 2. Encapsulation: Public/private data, provides control for how data is used
# 3. Polymorphism: 

# Object-oriented programming combines two things:
# 1. Data
# 2. Functionality

# You can put a function in a class, but not in a dictionary
# A class is the blueprint that you create objects with

class FootballPlayer:
    def __init__(self, firstname, lastname, position, team, scores):
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.team = team
        self.scores = scores

    def calc_scores(self):
        return self.scores *6

class FutbolPlayer(FootballPlayer):
    def calc_scores(self):
        return self.scores 
        
alvin_kamara = FootballPlayer("Alvin", "Kamara", "RB", "New Orleans Saints", 4)
nico_collins = FootballPlayer("Nico", "Collins", "WR", "Houston Texans", 1)
lionel_messi = FutbolPlayer("Lionel", "Messi", "F", "Argentina", 2)
pointsscored = 0

athletes = [alvin_kamara, nico_collins, lionel_messi]

for athlete in athletes:
    pointsscored += athlete.calc_scores()

print("points scored:", pointsscored)