import os
import pickle
from world.gamemap import World
print("Chose first command : 'start' or 'load' from file")
command_for_start = ""

while command_for_start != "start" or command_for_start != "load":
    command_for_start: str = str(input())
    try:
        if command_for_start == "start":
            garden = World([2, 2])
            count_of_plants = 3
            count_of_pests = 3
            count_of_trees = 3
            for i in range(0, count_of_pests):
                garden.add_pests_on_game_map()
            for i in range(0, count_of_plants):
                garden.add_plant_on_game_map()
            for i in range(0, count_of_trees):
                garden.add_trees_on_game_map()    
            for i in range(0, count_of_pests):
                garden.add_pests_on_game_map()
            for i in range(0, count_of_plants):
                garden.add_plant_on_game_map()
          
            print("Список команд:")
            print(" next_day -> следующий день\n add_plant -> добавить растение\n add_tree -> добавить дерево")
            print(" add_pests -> добавить вредителя\n water_plants -> полить растения\n save -> сохранить в файл\n")
            print("info -> информация об объекте\n delte_pests -> удалить всех вредителей")
            garden.step_print()
            break

        elif command_for_start == "load":
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
            print("Список команд:")
            print(" next_day -> следующий день\n add_plant -> добавить растение\n add_tree -> добавить дерево")
            print(" add_pests -> добавить вредителя\n water_plants -> полить растения\n save -> сохранить в файл\n")
            garden.step_print()
            break

        else:
            raise()
    except:
        print("Wrong command!!!")

command = ""

while command != "save":
    command = input()
    os.system("cls")
    print("Список команд:")
    print(" next_day -> следующий день\n add_plant -> добавить растение\n add_tree -> добавить дерево")
    print(" add_pests -> добавить вредителя\n water_plants -> полить растения\n save -> сохранить в файл\n")
    print(command)
    garden.commands(command)
    garden.step_print()

if command == "save":
    file = open(r'saved_game.txt', 'wb')
    pickle.dump(garden, file)
    for i in range(garden.map_size[0]):  # по строке
        for j in range(garden.map_size[1]):
            pickle.dump(garden.game_map[i][j], file)
    for smth in garden.plants:
        pickle.dump(smth, file)
    file.close()
    print("garden is saved")