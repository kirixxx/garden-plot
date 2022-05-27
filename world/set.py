class Sert():
    def __init__(self):
        pass
    
    def want_to_water_plants(self, garden):
        print("weather today:", garden.weather.weather_par)
        command = ""
        while command != "y" or command != "n":
            command = input("water plants? y/n\n")
            if command == "y":
                garden.commands("water_plants")
                break
            elif command == "n":
                print("no water")
                break
            else:
                print("Wrong command!")
                
    def commands(self, garden, command: str):
        try:
            if command == "garden_info":
                print("died from pests", garden.died_from_pests)
                print("died from hungry", garden.died_from_hungry)
                print("harvest of vegetables", garden.harvest_of_vegetables)
                print("harvest of fruits", garden.harvest_of_apples)
                garden.step_print()
            elif command == "weeding":
                for i in garden.plants:
                    garden.weeding()
                garden.count_of_days = 0
                garden.step_print()
            elif command == "next_day":
                garden.life_cycle()
                garden.count_of_days += 1
                if garden.count_of_days == 3:
                    for plant in garden.plants:
                        if plant.weed == False:
                            garden.getting_weed()
                garden.step_print()
            elif command == "add_plant":
                garden.add_plant_on_game_map()
                garden.step_print()
            elif command == "help":
                garden.fertilizing_game_map()
                garden.step_print()
            elif command == "add_tree":
                garden.add_trees_on_game_map()
                garden.step_print()
            elif command == "add_pests":
                garden.add_pests_on_game_map()
                garden.step_print()
            elif command == "water_plants":
                garden.watering_in_map()
            elif command == "delete_pests":
                for i in garden.plants:
                   if i.type_id == 2:
                       garden.delete_pest_from_garden()
                garden.step_print()
            elif command == "info":
                try:
                    x = input()
                    y = input()
                    z = input()
                    if int(x) <= int(garden.map_size[0]) and int(y) <= int(garden.map_size[1]):
                        garden.plants_info(x, y, z)
                    else:
                        raise()
                    garden.step_print()
                except:
                    print("Wrong coordinates")
            else:
                raise()
            garden.step_save()
        except:
            print("Wrong command")
            
    def plants_info(self, garden, position_x: int, position_y: int, position_z: int):
        x = int(position_x)
        y = int(position_y)
        count = int(position_z)
        if int(count) <= len(garden.game_map[x][y].all_in_cell):
            name = garden.game_map[x][y].all_in_cell[count].name
            print("name:" + name)
            age = garden.game_map[x][y].all_in_cell[count].age
            print("age:" + str(age))
            life_points = garden.game_map[x][y].all_in_cell[count].life_points
            print("life points:" + str(life_points))
            weed = garden.game_map[x][y].all_in_cell[count].weed
            print("weed: " + str(weed))
            if int(garden.game_map[x][y].all_in_cell[count].type_id) == 1 or int(garden.game_map[x][y].all_in_cell[count].type_id) == 3:
                points_to_grow = garden.game_map[x][y].all_in_cell[count].start_points
                print("points to grow up :" + str(points_to_grow))
                illness = garden.game_map[x][y].all_in_cell[count].illness
                print("illness :" + str(illness))
                watered = garden.game_map[x][y].all_in_cell[count].watered
                print("watered :" + str(watered))
            if int(garden.game_map[x][y].all_in_cell[count].type_id) == 2:
                damage = garden.game_map[x][y].all_in_cell[count].damage
                print("damage :" + str(damage))
                hungry = garden.game_map[x][y].all_in_cell[count].hungry
                print("hungry:" + str(hungry))
            print("-------------------------------------------")
        else:
            raise (print("Wrong coordinates <<z>>"))
       