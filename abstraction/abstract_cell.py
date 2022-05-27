from abc import ABC, abstractmethod
from abstraction.abstract_plant import AbstactPlant
class AbstractCell(ABC):
    def __init__(self):
        coordinates = tuple()
        all_in_cell = list()
        list_for_print = list()
        new_list = list()
        
    @abstractmethod
    def add_plant_on_cell(self, plant):
        pass
    
    @abstractmethod
    def add_weed_on_cell(self, count, plant):
        pass
    
    @abstractmethod
    def delete_weed_from_cell(self,count, plant):
        pass
    
    @abstractmethod
    def check_to_add_in_cell(self):
        pass
    
    @abstractmethod
    def print_cell(self):
        pass
    
    @abstractmethod
    def get_cell_position(self, smth, index: int):
        pass
    
    @abstractmethod
    def remove_smth_from_cell(self, smth: AbstactPlant):
        pass