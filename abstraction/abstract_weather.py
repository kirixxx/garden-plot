from abc import ABC, abstractmethod

class AbstactWeather(ABC):
    def __init__(self):
        self.weather_par = str
        self.type_of_weather = list()
        
    @abstractmethod
    def what_weather_today(self):
        pass