import os
import pickle

class RestoreService():
    def __init__(self):
        self.garden = None
    
    def restore_garden(self):
        file = open(r'saved_game.txt', 'rb')
        garden = pickle.load(file)
        for i in range(0, garden.map_size[0]):
            row = list()
            for j in range(0, garden.map_size[1]):
                Сell = pickle.load(file)
                for smth in Сell.all_in_cell:
                    garden.plants.append(smth)
                row.append(Сell)
            garden.game_map.append(row)
        for smth in range(1, len(garden.plants)):
            smth = pickle.load(file)
        file.close()
        garden.step_print()
        return garden