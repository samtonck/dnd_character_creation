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

        if user_input_class == 1:  # ПРИСЛУЖНИК
            player.strength = 8  # сила
            player.dexterity = 10  # ловкость
            player.constitution = 12  # телосложение
            player.intelligence = 15  # интелект
            player.wisdom = 14  # мудрость
            player.charisma = 13  # харизма
            player.skills = 'Владение навыками: Проницательность, Религия'  # навыки
            player.language += '+2 на ваш выбор'
            player.equipment += """Снаряжение: Священный символ (подаренный вам в момент принятия священного сана), 
молитвенник или молитвенный барабан, 5 палочек благовоний, облачение, комплект обычной одежды, поясной кошель с 15 зм"""
        elif user_input_class == 2:
            pass
        elif user_input_class == 3:  #
            pass
        elif user_input_class == 4:  #
            pass
        elif user_input_class == 5:  #
            pass
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
    12: ['Следопыт (Ranger)'],
    13: ['Чародей (Sorcerer)']
}
