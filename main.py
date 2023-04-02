def get_gameclass(n : int):
    dict_class = dict()
    list_class = []
    for _ in range(n):
        list_class.append(list(map(str, input().split("-"))))
        print(list_class)
    for i in list_class:
        dict_class[i[0]] = tuple(i[1:])
    return dict_class



def main():
    n = int(input())
    game_classes = get_gameclass(n)
    print(game_classes)
    choice_class(game_class)
main()

def choice_class(game_class : dict):
    print("Доступны классы:")
    for i in game_class:
        print(i)
    print("Укажите название класса:")
    c = input()
    for c in game_class:
        print("Вы выбрали - {}".format(c))
def choice_weapon():
    print("Вам доступно оружие:")
