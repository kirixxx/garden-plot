from abstraction.abstract_plant import AbstactPlant
import random

class Tree(AbstactPlant):
    def __init__(self, coordinates, garden):
        super().__init__(garden)
        self.index = 0
        self.type_id = 3
        self.name = "tree"
        self.symbol_on_map = "T"
        self.age = 0
        self.coordinates = coordinates
        self.max_age = 100
        self.life_points = 300
        self.points_to_grow = 8
        self.start_points = 0
        self.illness = False
        self.watered = False
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

    def grow_up(self, days: int):
        if self.weed:  #если есть сорняки
            if days <= 2:
                self.life_points -= 2
            if days > 2 and days <= 4:
                self.life_points -= 20
            if days > 4:
                self.life_points -= 50    
        if self.watered:  #растет только если полито
            self.start_points += 4
        if self.illness:  #если болезнь есть, то при росте отниметься 20 хп
            self.life_points -= 20
        if self.start_points >= self.points_to_grow and self.life_points > 100:
            self.start_points = 0
            return self

    def opportunity_to_live(self):
        if self.life_points <= 0:
            return self
        else:
            return None

    def get_illness_check(self):  #получение болезни (шанс 40%)
        self.illness = random.choices([True, False], weights=[40, 60], k=1)[0]
        return self

    def get_rid_of_illness_check(self):  #избавление от болезни (шанс 80%)
        self.illness = random.choices([True, False], weights=[20, 80], k=1)[0]
        return self

    def water(self):
        self.watered = True
        return self
    
    def attack_plant(self):
        return super().attack_plant()