import json
import os
from json import JSONDecodeError

from json_operation import read_json, write_json


def registration(user_name: str, json_data: dict):


    print("Вам нужно зарегистрироваться.")
    password = input("Введите пароль:")
    json_data[user_name] = password
    write_json(json_data,"users.json")
    final_registration(user_name)








def check_user(name_user: str, json_data: dict):
    return name_user in json_data


def autorization():
    json_data = read_json("users.json")
    name_user = input("Введите имя пользователя:")
    if check_user(name_user, json_data):
        password = input("Введите пароль:")
    else:
        registration(name_user, json_data)


def final_registration(name: str):
    game_dict = read_json("game_class.json")
    print("Доступны классы: ")
    count = 1
    for game_class in game_dict:
        print(f'{count} - {game_class}')
        count += 1
    my_class = input("Укажите игровой класс : ")
    count2 = 1
    print("Доступны оружия: ")
    for game_weapon in game_dict[my_class]:
        print(f'{count2} - {game_weapon}')
        count2 += 1
    my_weapon = input("Укажите игровое оружие : ")
    print(f"Ваш ник - {name}, Ваш класс - {my_class} , Ваше оружие - {my_weapon}")




