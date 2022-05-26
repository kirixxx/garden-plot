import random

class Weather:    
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
