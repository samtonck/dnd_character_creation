import random as random
import player


def input_race():
    print('Шаг 3: Выбор расы')
    for number, name in game_race.items():
        print(' {num:^5} |    {name} '.format(num=number, name=name[0]))
    print()

    user_input_race = int(input('Введите номер расы: '))

    while user_input_race not in game_race:
        print('Такой расы нет')
        user_input_race = int(input("Введите номер расы: "))
    else:
        print('Вы выбрали расу', game_race[user_input_race][0], '\n')
        name_race = game_race[user_input_race][0]
        player.race = name_race
        if user_input_race == 1:  # Лесной гном
            forest_gnome()
        elif user_input_race == 2:  # Скальный гном
            rock_gnome()
        elif user_input_race == 3:  # Дворф
            dwarf()
        elif user_input_race == 4:  # Горный дворф
            mountain_dwarf()
        elif user_input_race == 5:  # Холмовой дворф
            hill_dwarf()
        elif user_input_race == 6:  # Драконорожденнй
            dragonborn()
        elif user_input_race == 7:  # Полуорк
            half_orc()
        elif user_input_race == 8:  # Полурослик
            halfling()
        elif user_input_race == 9:  # Коренастый полурослик
            chunky_halfling()
        elif user_input_race == 10:  # Легконогий полурослик
            lightfoot_halfling()
        elif user_input_race == 11:  # Полуэльф
            half_elf()
        elif user_input_race == 12:  # Тифлинг
            tiefling()
        elif user_input_race == 13:  # Человек
            human()
        elif user_input_race == 14:  # Эльф
            elf()
        elif user_input_race == 15:  # Высший эльф
            high_elf()
        elif user_input_race == 16:  # Лесной эльф
            forest_elf()
        elif user_input_race == 17:  # Темный эльф
            dark_elf()
    return name_race


game_race = {
    1: ['Лесной гном (Forest gnome)'],
    2: ['Скальный гном (Rock gnome)'],
    3: ['Дварф (Dwarf)'],
    4: ['Горный дварф (Mountain dwarf)'],
    5: ['Холмовой дварф (Hill dwarf)'],
    6: ['Драконорожденный (Dragonborn)'],
    7: ['Полуорк (Half-orc)'],
    8: ['Полурослик (Halfling)'],
    9: ['Коренастый полурослик (Chunky halfling)'],
    10: ['Легконогий полурослик (Lightfoot halfling)'],
    11: ['Полуэльф (Half-elf)'],
    12: ['Тифлинг (Tiefling)'],
    13: ['Человек (Human)'],
    14: ['Эльф (Elf)'],
    15: ['Высший эльф (High elf)'],
    16: ['Лесной эльф (Forest elf)'],
    17: ['Темный эльф (Dark elf)']
}


def forest_gnome():
    player.intelligence += 2
    player.dexterity += 1
    player.age = random.randrange(40, 500)
    player.alignment = """Гномы чаще всего добры. Стремящиеся к порядку обычно становятся мудрецами, инженерами, 
исследователями, учёными или изобретателями. Те, кто больше склонны к хаосу, становятся менестрелями, мошенниками, 
путешественниками или искусными  ювелирами. Гномы добросердечны, и даже мошенники из них получаются скорее шутливые, 
чем злобные.
"""
    player.height = random.randrange(91, 122)
    player.weight = random.randrange(15, 20)
    player.speed = 25
    player.dark_vision = 60
    player.check_saving_throws_intelligence = True  # спас бросок интелект
    player.check_saving_throws_wisdom = True  # спас бросок мудрость
    player.check_saving_throws_charisma = True  # спас бросок харизма
    player.language += """Вы можете говорить, читать и писать на Общем и Гномьем языках. Гномий язык, использующий 
дварфский алфавит, хорошо известен благодаря техническим трактатам и каталогам знаний об окружающем мире.
"""
    player.other += """Природная иллюзия. Вы знаете заклинание малая иллюзия. Базовой характеристикой для его 
использования является Интеллект. Общение с маленькими зверями. С помощью звуков и жестов вы можете передавать простые 
понятия Маленьким или ещё меньшим зверям. Лесные гномы любят животных и часто держат белок, барсуков, кроликов, кротов, 
дятлов и других животных в качестве питомцев.
"""


def rock_gnome():
    player.intelligence += 2
    player.constitution += 1
    player.age = random.randrange(40, 500)
    player.alignment = """Гномы чаще всего добры. Стремящиеся к порядку обычно становятся мудрецами, инженерами, 
исследователями, учёными или изобретателями. Те, кто больше склонны к хаосу, становятся менестрелями, мошенниками, 
путешественниками или искусными ювелирами. Гномы добросердечны, и даже мошенники из них получаются скорее шутливые, чем 
злобные.
"""
    player.height = random.randrange(91, 122)
    player.weight = random.randrange(15, 20)
    player.speed = 25
    player.dark_vision = 60
    player.check_saving_throws_intelligence = True  # спас бросок интелект
    player.check_saving_throws_wisdom = True  # спас бросок мудрость
    player.check_saving_throws_charisma = True  # спас бросок харизма
    player.language += """Вы можете говорить, читать и писать на Общем и Гномьем языках. Гномий язык, использующий 
дварфский алфавит, хорошо известен благодаря техническим трактатам и каталогам знаний об окружающем мире.
"""
    player.other += """Ремесленные знания. При совершении проверки Интеллекта (История) применительно к магическому, 
алхимическому или технологическому объекту, вы можете добавить к проверке удвоенный бонус мастерства вместо обычного. 
Жестянщик. Вы владеете ремесленными инструментами (инструменты жестянщика). С их помощью вы можете, потратив 1 час 
времени и материалы на сумму в 10 зм, создать Крошечное механическое устройство (КД 5, 1 хит). Это устройство перестаёт 
работать через 24 часа (если вы не потратите 1 час на поддержание его работы). Вы можете действием разобрать его; в 
этом случае вы можете получить обратно использованные материалы. Одновременно вы можете иметь не более трёх таких 
устройств. При создании устройства выберите один из следующих вариантов: Заводная игрушка. Эта заводная игрушка 
изображает животное, чудовище или существо, вроде лягушки, мыши, птицы, дракона или солдатика. Поставленная на землю, 
она проходит 5 фт. в случайном направлении за каждый ваш ход, издавая звуки, соответствующие изображаемому существу. 
Зажигалка. Это устройство производит миниатюрный огонёк, с помощью которого можно зажечь свечу, факел или костёр. 
Использование этого устройства требует действия. Музыкальная шкатулка. При открытии эта шкатулка проигрывает мелодию 
средней громкости. Шкатулка перестаёт играть если мелодия закончилась или если шкатулку закрыли.
"""


def dwarf():
    pass


def mountain_dwarf():
    pass


def hill_dwarf():
    pass


def dragonborn():
    pass


def half_orc():
    pass


def halfling():
    pass


def chunky_halfling():
    pass


def lightfoot_halfling():
    pass


def half_elf():
    pass


def tiefling():
    pass


def human():
    pass


def elf():
    pass


def high_elf():
    pass


def forest_elf():
    pass


def dark_elf():
    pass
