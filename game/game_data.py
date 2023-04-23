import json
import os

def save_data_class(dict_class : dict):
    if os.path.exists("game_class.json"):
        os.remove("game_class.json")
    with open("game_class.json","w") as f:
        json.dump(dict_class,f)
def get_game_class(file_name : str):
    with open(file_name, "r") as f:
        n = int(f.readline())
    dict_class = dict()
    list_class = []
    for _ in range(n):
        list_class.append(f.readline().encode("cp1251").decode().strip("\n").split("-"))
        print(list_class)
    for i in list_class:
        dict_class[i[0]] = tuple(i[1:])
    print(dict_class)
    save_data_class()