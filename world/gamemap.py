from typing import Set
from mobs.tree import Tree
from mobs.vegetables import Carrot
from mobs.pest import Pest
from mobs.weather import Weather
import random
import pickle
from world.cell import Cell
from world.set import Sert

class World:
    game_map = list()
    map_size = tuple()
    plants = list()
    weather = Weather()
    step = 0
    harvest_of_vegetables = 0
    harvest_of_apples = 0
    died_from_pests = 0
    died_from_hungry = 0
    died_from_illness = 0
    weather_today_is = ""
    index = 0
    count_of_days = 0
    map_open_position = tuple()
    sert = Sert()
    
    def __init__(self, map_size: tuple = [2,2]):
        self.map_size = map_size
        for i in range(0, map_size[0]):
            row = list()
            for j in range(0, map_size[1]):
                row.append(Cell([i, j]))
            self.game_map.append(row)

    def start_garden(self):
        count_of_plants = 3
        count_of_pests = 3
        count_of_trees = 3
        for i in range(0, count_of_pests):
            self.add_pests_on_game_map()
        for i in range(0, count_of_plants):
            self.add_plant_on_game_map()
        for i in range(0, count_of_trees):
            self.add_trees_on_game_map()
        for i in range(0, count_of_pests):
            self.add_pests_on_game_map()
        for i in range(0, count_of_plants):
            self.add_plant_on_game_map()
        self.step_print()
        
    def find_open_position(self):
        x = random.randint(0, self.map_size[0] - 1)
        y = random.randint(0, self.map_size[1] - 1)
        if not self.game_map[x][y].check_to_add_in_cell():
            return self.find_open_position()
        else:
            return (x, y)

    def find_plant_position(self):
        for x in range(self.map_size[0]):
            for y in range(self.map_size[1]):
                if self.game_map[x][y].check_to_add_in_cell():
                    return (x, y)
                else: 
                    continue

    def check_to_add(self):
        a = int(self.map_size[0])
        b = int(self.map_size[1])
        return len(self.plants) < 4 * a * b


    def add_pests_on_game_map(self):
        if self.check_to_add():
            new_plant = Pest(self.find_plant_position(), self)
            self.index += 1
            new_plant.index = self.index
            self.plants.append(new_plant)
            x = int(new_plant.coordinates[0])
            y = int(new_plant.coordinates[1])
            self.game_map[x][y].add_plant_on_cell(new_plant)
        else:
            print("No place!")

    def add_plant_on_game_map(self):
        if self.check_to_add():
            new_plant = Carrot(self.find_plant_position(), self)
            self.index += 1
            new_plant.index = self.index
            self.plants.append(new_plant)
            x = int(new_plant.coordinates[0])
            y = int(new_plant.coordinates[1])
            self.game_map[x][y].add_plant_on_cell(new_plant)
        else:
            print("No place!")

    def add_trees_on_game_map(self):
        if self.check_to_add():
            new_plant = Tree(self.find_plant_position(), self)
            self.index += 1
            new_plant.index = self.index
            self.plants.append(new_plant)
            x = int(new_plant.coordinates[0])
            y = int(new_plant.coordinates[1])
            self.game_map[x][y].add_plant_on_cell(new_plant)
        else:
            print("No place!")

    def step_print(self):
        for row in self.game_map:
            for Cell in row:
                print(Cell.print_cell())

    def aging_in_map(self):
        for smth in self.plants:
            smth = smth.aging()
            if smth is not None:
                self.plants.remove(smth)
                smth.get_position()
                x = int(smth.coordinates[0])
                y = int(smth.coordinates[1])
                self.game_map[x][y].remove_smth_from_cell(smth)

    def plants_grow_up(self):
        for smth in self.plants:
            if smth.type_id == 1:
               self.plants_grow(smth)
                    
    def plants_grow(self, plant):
        if self.weather.weather_par == "sun":
            plant = plant.get_rid_of_illness_check()
            plant = plant.grow_up(self.count_of_days)
        if self.weather.weather_par == "rain":
            plant = plant.get_illness_check()
            plant = plant.grow_up(self.count_of_days)
        if self.weather.weather_par == "drought":
            if not plant.watered:
                plant.life_points -= 10
            if plant.watered:
                plant = plant.grow_up(self.count_of_days)
        if plant is not None:
            self.harvest_of_vegetables += 1
            self.plants.remove(plant)
            plant.get_position()
            x = int(plant.coordinates[0])
            y = int(plant.coordinates[1])
            self.game_map[x][y].remove_smth_from_cell(plant)

    def trees_grow_up(self):
        for tree in self.plants:
            if tree.type_id == 3:
                self.tree_grow(tree)
    
    def tree_grow(self, tree):
        if self.weather.weather_par == "sun":
            tree = tree.get_rid_of_illness_check()
            tree = tree.grow_up(self.count_of_days)
        if self.weather.weather_par == "rain":
            tree = tree.get_illness_check()
            tree = tree.grow_up(self.count_of_days)
        if self.weather.weather_par == "drought":
            if not tree.watered:
                tree.life_points -= 20
            if tree.watered:
                tree = tree.grow_up(self.count_of_days)
            if tree is not None:
                    self.harvest_of_apples += 1       
                                
    def eat_plant_on_map(self):
        for pests in self.plants:
            if pests.type_id == 2:
                pests.get_position()
                for plant_for_eat in self.plants:
                    self.eat_plant(pests, plant_for_eat)

    def eat_plant(self, pests, plant_for_eat):
        if plant_for_eat.type_id == 1:
            plant_for_eat.get_position()
            if int(plant_for_eat.coordinates[0]) == int(pests.coordinates[0]) and int(plant_for_eat.coordinates[1]) == int(pests.coordinates[1]):
                plant_for_eat = pests.attack_plant(plant_for_eat)
                if plant_for_eat is not None:
                    self.died_from_pests += 1
                    self.plants.remove(plant_for_eat)
                    self.game_map[int(plant_for_eat.coordinates[0])][int(plant_for_eat.coordinates[1])].remove_smth_from_cell(plant_for_eat)
            
    def damage_trees_on_map(self):
        for pests in self.plants:
            if pests.type_id == 3:
                pests.get_position()
                for plant_for_eat in self.plants:
                    self.eat_tree(plant_for_eat, pests)
                    
           
    def eat_tree(self,plant_for_eat, pests):
        if plant_for_eat.type_id == 1:
            plant_for_eat.get_position()
            if int(plant_for_eat.coordinates[0]) == int(pests.coordinates[0]) and int(plant_for_eat.coordinates[1]) == int(pests.coordinates[1]):
                plant_for_eat = pests.attack_plant(plant_for_eat)
                if plant_for_eat is not None:
                    self.died_from_pests += 1
                    self.plants.remove(plant_for_eat)
    
    def opportunity_to_live_on_map(self):
        for smth in self.plants:
            if smth.type_id == 2:
                smth = smth.opportunity_to_live()
                if smth is not None:
                    smth.get_position()
                    x = int(smth.coordinates[0])
                    y = int(smth.coordinates[1])
                    self.game_map[x][y].remove_smth_from_cell(smth)
                    self.plants.remove(smth)
                    self.died_from_hungry += 1

    def everydays_hungry(self):
        for pests in self.plants:
            if pests.type_id == 2:
                pests.hungry = True

    def watering_in_map(self):
        for smth in self.plants:
            if smth.type_id == 1 or smth.type_id == 3:
                smth = smth.water()
        print("Plants watered!")

    def life_cycle(self):
        self.weather.weather_today(self)
        self.sert.want_to_water_plants(self)
        self.plants_grow_up()
        self.trees_grow_up()
        self.eat_plant_on_map()
        self.aging_in_map()
        self.opportunity_to_live_on_map()
        self.everydays_hungry()

    def step_save(self):
        file = open(r'saved_game.txt', 'wb')
        pickle.dump(self, file)
        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                pickle.dump(self.game_map[i][j], file)
        for smth in self.plants:
            pickle.dump(smth, file)
        file.close()

    def plants_info(self, position_x: int, position_y: int, position_z: int):
        self.sert.plants_info(self, position_x, position_y, position_z)
       
    def delete_pest_from_garden(self):
        for pests in self.plants:
            if pests.type_id == 2:
                pests.life_points = 0
                pests = pests.opportunity_to_live()
                if pests is not None:
                    pests.get_position()
                    x = int(pests.coordinates[0])
                    y = int(pests.coordinates[1])
                    self.game_map[x][y].remove_smth_from_cell(pests)
                    self.plants.remove(pests)

    def weeding(self):
        for plant in self.plants:
            if plant.type_id == 1 or plant.type_id == 2 or plant.type_id == 3:
                plant.get_position()
                plant.weed = False
                x = int(plant.coordinates[0])
                y = int(plant.coordinates[1])
                index = plant.index
                count = self.game_map[x][y].get_cell_position(plant, index)
                self.game_map[x][y].delete_weed_from_cell(count, plant)
            
    def getting_weed(self):
        for plant in self.plants:
                plant.weed = True
                plant.get_position()
                x = int(plant.coordinates[0])
                y = int(plant.coordinates[1])
                index = plant.index
                count = self.game_map[x][y].get_cell_position(plant, index )
                self.game_map[x][y].add_weed_on_cell(count, plant)
    
    def fertilizing_game_map(self):
        for plant in self.plants: 
            if plant.type_id == 1:
                plant.life_points = 100
                plant.points_to_grow += 5
            if plant.type_id == 3:
                plant.life_points = 300
                plant.points_to_grow += 4
                         
    def commands(self, command: str):
        self.sert.commands(self, command)
