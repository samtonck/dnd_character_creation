import random as random
import player


def input_class():
    print('Шаг 4: Выбор класса')
    for number, name in game_class.items():
        print(' {num:^5} |    {name} '.format(num=number, name=name[0]))
    print()

    user_input_class = int(input('Введите номер класса: '))

    while user_input_class not in game_class:
        print('Такого класса нет')
        user_input_class = int(input("Введите номер класса: "))
    else:
        print('Вы выбрали класс', game_class[user_input_class][0], '\n')
        name_class = game_class[user_input_class][0]
        player.game_class = name_class

        if user_input_class == 1:  # Бард
            bard()
        elif user_input_class == 2:  # Варвар
            barbarian()
        elif user_input_class == 3:  # Воин
            fighter()
        elif user_input_class == 4:  # Волшебник
            wizard()
        elif user_input_class == 5:  # Друид
            druid()
        elif user_input_class == 6:  # Жрец
            cleric()
        elif user_input_class == 7:  # Колдун
            warlock()
        elif user_input_class == 8:  # Монах
            monk()
        elif user_input_class == 9:  # Паладин
            paladin()
        elif user_input_class == 10:  # Плут
            rogue()
        elif user_input_class == 11:  # Следопыт
            ranger()
        elif user_input_class == 12:  # Чародей
            sorcerer()
    return name_class


game_class = {
    1: ['Бард (Bard)'],
    2: ['Варвар (Barbarian)'],
    3: ['Воин (Fighter)'],
    4: ['Волшебник (Wizard)'],
    5: ['Друид (Druid)'],
    6: ['Жрец (Cleric)'],
    7: ['Колдун (Warlock)'],
    8: ['Монах (Monk)'],
    9: ['Паладин (Paladin)'],
    10: ['Плут (Rogue)'],
    11: ['Следопыт (Ranger)'],
    12: ['Чародей (Sorcerer)']
}


def bard():  # Бард
    player.strength = 8  # сила
    player.dexterity = 10  # ловкость
    player.constitution = 12  # телосложение
    player.intelligence = 15  # интелект
    player.wisdom = 14  # мудрость
    player.charisma = 13  # харизма
    player.skills = """Владение навыками: Проницательность, Религия
    """  # навыки
    player.language += """+2 на ваш выбор
    """
    player.equipment += """Снаряжение: Священный символ (подаренный вам в момент принятия священного сана), 
молитвенник или молитвенный барабан, 5 палочек благовоний, облачение, комплект обычной одежды, поясной кошель с 15 зм
"""


def barbarian():  # Варвар
    pass


def fighter():  # Воин
    pass


def wizard():  # Волшебник
    pass


def druid():  # Друид
    pass


def cleric():  # Жрец
    pass


def warlock():  # Колдун
    pass


def monk():  # Монах
    pass


def paladin():  # Паладин
    pass


def rogue():  # Плут
    pass


def ranger():  # Следопыт
    pass


def sorcerer():  # Чародей
    pass

