from abstraction.abstract_cell import AbstractCell
from abstraction.abstract_plant import AbstactPlant

class Cell(AbstractCell):
        def __init__(self, coordinates: tuple):
            self._coordinates = coordinates
            self.all_in_cell = list()
            self.list_for_print = list()

        def add_plant_on_cell(self, plant):
            if len(self.all_in_cell) < 4:
                self.all_in_cell.append(plant)
                self.list_for_print.append(plant.symbol_on_map)
            else:
                return
  
        def add_weed_on_cell(self, count, plant):
            if self.all_in_cell[count].type_id == 1:
                d = "C!"
            if self.all_in_cell[count].type_id == 2:
                d = "P!"
            if self.all_in_cell[count].type_id == 3:
                d = "T!"
            self.list_for_print.pop(count)
            self.list_for_print.insert(count, d)
            
        def delete_weed_from_cell(self,count, plant):
            self.list_for_print.pop(count)
            self.list_for_print.insert(count, plant.symbol_on_map)
               
        def check_to_add_in_cell(self):
            if len(self.all_in_cell) < 4:
                return True
            else:
                return False

        def print_cell(self):
            if len(self.list_for_print) != 0:
                return self.list_for_print
            
            else:
                return "*"                

        def get_cell_position(self, smth, index: int):
            count = 0
            for plant in self.all_in_cell:
                if plant.type_id == smth.type_id and plant.index == index :
                    return count
                else:
                    count += 1

        def remove_smth_from_cell(self, smth: AbstactPlant):
            for i in  self.all_in_cell:
                if i.index ==  smth.index:
                    self.all_in_cell.remove(i)
                    self.list_for_print.remove(i.symbol_on_map)