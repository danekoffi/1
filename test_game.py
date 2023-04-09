import sys

from game.game_data import get_game_class


def main():
    if len(sys.argv) == 3:
        if sys.argv[1] == "-gamesetting":
            get_game_class(sys.argv[2])
        else:
            print("Неверная команда.")
    elif len(sys.argv) == 1:
        autorization()
    else:
        print("Неверная команда.")

if __name__ == "__main__":
    main()
# def main():
#     n = int(input())
#     game_classes = get_gameclass(n)
#     print(game_classes)
#     choice_class(game_class)
# main()
#
# def choice_class(game_class : dict):
#     print("Доступны классы:")
#     for i in game_class:
#         print(i)
#     print("Укажите название класса:")
#     c = input()
#     for c in game_class:
#         print("Вы выбрали - {}".format(c))
# def choice_weapon():
#     print("Вам доступно оружие:")
