import json
import os
from json import JSONDecodeError

def registration(user_name : str, dict_users : dict):
    print("Вам нужно зарегистрироваться.")
    password = input("Введите пароль:")
    dict_users[user_name] = password
    save_user(dict_users)
    final_registration(user_name)



def get_users():
    if os.path.exists("users.json"):
     try:
        with open("users.json","r") as f:
            dict_users = json.load(f)
            return dict_users
     except JSONDecodeError:
        return {}
    else:
        return {}

def save_user(dict_user : dict):
    with open("users.json","w") as file_json:
        json.dump(dict_user, file_json)
def check_user(name_user : str, dict_users : dict):
    return name_user in dict_users


def autorization():
    dict_users = get_users()
    name_user = input("Введите имя пользователя:")
    if check_user(name_user, dict_users):
        password = input("Введите пароль:")
    else:
        registration(name_user,dict_users)

def get_game_class():
    if os.path.exists("game_class.json"):
     try:
        with open("game_class.json","r", encoding = "utf-8") as f:
            dict_users = json.load(f)
            return dict_users
     except JSONDecodeError:
        return {}
    else:
        return {}
def final_registration(name : str):
    game_dict = get_game_class()
    print("Доступны классы: ")
    print(game_dict.keys())
    my_class = input("Укажите игровой класс : ")
    if my_class in game_dict:
        print("Выберите оружие: ")
        print(*game_dict[my_class])
        my_weapon = input("Укажите игровое оружие : ")
        print(f"Ваш ник - {name}, Ваш класс - {my_class} , Ваше оружие - {my_weapon}")







