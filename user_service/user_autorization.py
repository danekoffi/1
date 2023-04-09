import json
import os

def get_users():
    if os.path.exists("users.json"):
     try:
        with open("user.json","r") as f:
            dict_users = json.load(f)
            return dict_users
     except:
        return dict()
    else:
        return dict()

def autorization():
    name_user = input("Введите имя пользователя:")