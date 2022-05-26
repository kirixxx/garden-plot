from Plant import MainClass

class Pest(MainClass):
    def __init__(self, coordinates: tuple, garden):
        super().__init__(garden)
        self.index = 0
        self.type_id = 2
        self.name = "pests"
        self.symbol_on_map = "P"
        self.age = 0
        self.coordinates = coordinates
        self.max_age = 10
        self.life_points = 100
        self.damage = 40
        self.hungry = True
        self.weed = False

    def aging(self):
        self.age += 1
        if self.age >= self.max_age:
            return self
        else:
            return None

    def get_position(self):
        x = self.coordinates[0]
        y = self.coordinates[1]
        return (x, y)

    def attack_plant(self, plant_for_eat):
        self.hungry = False
        plant_for_eat.life_points -= self.damage
        if self.life_points == 100:
            self.life_points == 100
        else:
            self.life_points += 10
        if plant_for_eat.life_points <= 0:
            return plant_for_eat
        else:
            return None

    def opportunity_to_live(self):
        if self.weed:
            self.life_points -= 20
        if self.hungry:
            self.life_points -= 40
        if self.life_points <= 0:
            return self
        else:
            return None
