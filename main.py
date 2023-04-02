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


name=input("Введите имя вашего персонажа:")
count_klass="1 - Маг , 2 - Воин , 3 - Паладин , 4 - Злодей"
print(count_klass)
klass=input("Выберите и введите класс персонажа(напишите НАЗВАНИЕ класса):")
count_armanent="1 - Посох Веры , 2 - Палочка справедливости , 3 - Средневековый меч"
print(count_armanent)
armanent=input("Выберите и введите название стартового оружия(напишите НАЗВАНИЕ оружия):")

print("Добро пожаловать в игру , {} ".format(name))
print()

