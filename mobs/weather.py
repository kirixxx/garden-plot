import random

from abstraction.abstract_weather import AbstactWeather

class Weather(AbstactWeather):    
    def __init__(self, world=None):
        if world is not None:
            self.world = world
        self.weather_par = ""
        self.type_of_weather = ["sun", "rain"]

    def what_weather_today(self):
        weather_today = random.choice(self.type_of_weather)
        if self.weather_par == "sun" and weather_today == "sun":
            weather_today = "drought"
        if self.weather_par == "drought" and weather_today == "sun":
            weather_today = "drought"
        self.weather_par = weather_today
        return self.weather_par
    
    def weather_today(self, garden):
        garden.weather.what_weather_today()
        if garden.weather.weather_par == "sun" or garden.weather.weather_par == "drought":
            for smth in garden.plants:
                smth.watered = False
        if garden.weather.weather_par == "rain":
            for smth in garden.plants:
                smth.watered = True
        return garden.weather.weather_par