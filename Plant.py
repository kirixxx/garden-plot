from abc import ABC, abstractmethod
class MainClass(ABC):

    def __init__(self, world=None):
        if world is not None:
            self.world = world
        self.index = 0
        self.type_id = 0
        self.name = ""
        self.symbol_on_map = ""
        self.age = 0
        self.coordinates = tuple()
        self.max_age = 0
        self.life_points = 0
        self.factor_grow_up = 0
        self.factor_plants = 0
        self.factor_pests = 0
        self.hungry = True
        self.weed = False
        
    def attack_plant(self):
        pass

    def aging(self):
        pass

    def get_position(self):
        pass

    def grow_up(self):
        pass

    def opportunity_to_live(self):
        pass



