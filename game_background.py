import random as random
import player


def input_background():
    print('Шаг 5: Выбор предыстории')
    for number, name in game_class.items():
        print(' {num:^5} |    {name} '.format(num=number, name=name[0]))
    print()

    user_input_background = int(input('Введите номер предыстории: '))

    while user_input_background not in game_class:
        print('Такой предыстории нет')
        user_input_background = int(input("Введите номер предыстории: "))
    else:
        print('Вы выбрали предысторию', game_class[user_input_background][0], '\n')
        name_background = game_class[user_input_background][0]
        player.background = name_background
    return name_background


game_class = {
    1: ['ПРИСЛУЖНИК'],
    2: ['ШАРЛАТАН'],
    3: ['ПРЕСТУПНИК'],
    4: ['АРТИСТ'],
    5: ['НАРОДНЫЙ ГЕРОЙ'],
    6: ['ГИЛЬДЕЙСКИЙ РЕМЕСЛЕННИК'],
    7: ['ОТШЕЛЬНИК'],
    8: ['БЛАГОРОДНЫЙ'],
    9: ['ЧУЖЕЗЕМЕЦ'],
    10: ['МУДРЕЦ'],
    12: ['МОРЯК'],
    13: ['СОЛДАТ'],
    14: ['БЕСПРИЗОРНИК']
}
