from Plant import MainClass
import random
class Carrot(MainClass):
    def __init__(self, coordinates: tuple, garden):
        super().__init__(garden)
        self.index = 0
        self.type_id = 1
        self.name = "carrot"
        self.symbol_on_map = "C"
        self.age = 0
        self.coordinates = coordinates
        self.max_age = 8
        self.life_points = 100
        self.points_to_grow = 12
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
            self.start_points += 3
        if self.illness:  #если болезнь есть, то при росте отниметься 10 хп
            self.life_points -= 10
        if self.points_to_grow <= self.start_points and self.life_points > 15:
            return self
        else:
            return None

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
        if not self.watered:  #если watered == false, то
            self.watered = True
        else:
            self.life_points -= 10  #если растение уже было полито (watered == True), то отнимаем 10 хп
        return self
