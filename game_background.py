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

        if user_input_background == 1:  # ПРИСЛУЖНИК
            servant()
            servant_background()
        elif user_input_background == 2:  # ШАРЛАТАН
            charlatan()
            charlatan_background()
        elif user_input_background == 3:  # ПРЕСТУПНИК
            criminal()
            criminal_background()
        elif user_input_background == 4:  # АРТИСТ
            artist()
            artist_background()
        elif user_input_background == 5:  # НАРОДНЫЙ ГЕРОЙ
            folk_hero()
            folk_hero_background()
        elif user_input_background == 6:  # ГИЛЬДЕЙСКИЙ РЕМЕСЛЕННИК
            guild_craftsmen()
            guild_craftsmen_background()
        elif user_input_background == 7:  # ОТШЕЛЬНИК
            hermit()
            hermit_background()
        elif user_input_background == 8:  # БЛАГОРОДНЫЙ
            noble()
            noble_background()
        elif user_input_background == 9:  # ЧУЖЕЗЕМЕЦ
            aliens()
            aliens_background()
        elif user_input_background == 10:  # МУДРЕЦ
            sage()
            sage_background()
        elif user_input_background == 11:  # МОРЯК
            sailor()
            sailor_background()
        elif user_input_background == 12:  # СОЛДАТ
            soldier()
            soldier_background()
        elif user_input_background == 13:  # БЕСПРИЗОРНИК
            throwaway()
            throwaway_background()

    return name_background


game_class = {
    1: ['ПРИСЛУЖНИК (Servant)'],
    2: ['ШАРЛАТАН (Charlatan)'],
    3: ['ПРЕСТУПНИК (Criminal)'],
    4: ['АРТИСТ (Artist)'],
    5: ['НАРОДНЫЙ ГЕРОЙ (Folk hero)'],
    6: ['ГИЛЬДЕЙСКИЙ РЕМЕСЛЕННИК (Guild craftsmen)'],
    7: ['ОТШЕЛЬНИК (Hermit)'],
    8: ['БЛАГОРОДНЫЙ (Noble)'],
    9: ['ЧУЖЕЗЕМЕЦ (Aliens)'],
    10: ['МУДРЕЦ (Sage)'],
    11: ['МОРЯК (Sailor)'],
    12: ['СОЛДАТ (Soldier)'],
    13: ['БЕСПРИЗОРНИК (Throwaway)']
}


#  ++++++++++++++++++++++++++++++++++++++++  background_pick  ++++++++++++++++++++++++++++++++++++++++
def servant():  # ПРИСЛУЖНИК

    player.check_insight = True  # знание проницательность
    player.check_religion = True  # знание религия
    player.language += """+2 на ваш выбор
"""
    player.equipment += """
Священный символ (подаренный вам в момент принятия священного сана), молитвенник или молитвенный барабан, 5 палочек 
благовоний, облачение, комплект обычной одежды, поясной кошель с 15 зм
"""


def charlatan():  # ШАРЛАТАН
    pass


def criminal():  # ПРЕСТУПНИК
    pass


def artist():  # АРТИСТ
    pass


def folk_hero():  # НАРОДНЫЙ ГЕРОЙ
    pass


def guild_craftsmen():  # ГИЛЬДЕЙСКИЙ РЕМЕСЛЕННИК
    pass


def hermit():  # ОТШЕЛЬНИК
    pass


def noble():  # БЛАГОРОДНЫЙ
    pass


def aliens():  # ЧУЖЕЗЕМЕЦ
    pass


def sage():  # МУДРЕЦ
    pass


def sailor():  # МОРЯК
    pass


def soldier():  # СОЛДАТ
    pass


def throwaway():  # БЕСПРИЗОРНИК
    pass


#  ++++++++++++++++++++++++++++++++++++++++  background_create  ++++++++++++++++++++++++++++++++++++++++
def servant_background():  # ПРИСЛУЖНИК
    background_personality_traits_list = {  # черты характера
        1: ['Я идеализирую конкретного героя своей веры и постоянно ссылаюсь на его поступки и свершения'],
        2: ['Я могу найти общую позицию  у самых яростных врагов, сопереживая им, и всегда стремясь к примирению'],
        3: ['Я вижу знамения в каждом событии и поступке.Боги пытаются говорить с нами, нужно лишь прислушаться'],
        4: ['Ничто не может поколебать мой оптимизм'],
        5: ['При любой оказии я цитирую(или перевираю) священные тексты и притчи'],
        6: ['Я терпим(или нетерпим) к другим верованиям, и уважаю(или порицаю) поклонение другим богам'],
        7: ['Я люблю хорошую еду, выпивку и высокое общество представителей своего храма.Жизнь вдали от этого меня '
            'раздражает'],
        8: ['Я пробыл в храме слишком долго, и мне недостаёт опыта взаимодействия с людьми за его пределами']
    }

    background_ideals_list = {  # идеалы
        1: ['Традиции. Мы должны сохранить и защитить древние традиции богослужения и совершения священных таинств '
            '(Законный)'],
        2: ['Милосердие. Несмотря на затраченные усилия, я всегда пытаюсь помочь тем, кто в нужде (Добрый)'],
        3: ['Перемены. Мы должны помогать привносить в мир перемены, которых наши божества постоянно жаждут '
            '(Хаотичный)'],
        4: ['Власть. Я надеюсь однажды подняться на самую вершину своей религиозной иерархии (Законный)'],
        5: ['Вера. Я верю, что моё божество направляет меня. И что усердная работа всегда будет вознаграждена '
            '(Законный)'],
        6: ['Стремление. Я ищу шанс доказать, что я достоин благословения своего божества, совершая деяния в '
            'соответствии с его учениями (Любой)']
    }

    background_bonds_list = {  # привязанности
        1: ['Я не пощажу живота своего, лишь бы найти древнюю реликвию своей веры, что была потеряна давным давно'],
        2: ['Однажды я отомщу развращённым представителям верховной иерархии своего храма, что объявили меня еретиком'],
        3: ['Я обязан своей жизнью священнику, который позаботился обо мне, когда умерли родители'],
        4: ['Всё, что я делаю — для простых людей'],
        5: ['Я пойду на всё что угодно, дабы защитить свой храм'],
        6: ['Я пытаюсь сохранить священные тексты, которые мои враги считают еретическими и пытаются уничтожить'],
    }

    background_flaws_list = {  # слабости
        1: ['Я не проявляю снисходительности к другим, но к себе я ещё более суров'],
        2: ['Я слишком доверяю тем, кто обладает властью в моей церковной иерархии'],
        3: ['Моя набожность зачастую приводит к тому, что я слепо верю всем, кто исповедует мою религию'],
        4: ['Я непреклонен в своих убеждениях'],
        5: ['Я настороженно отношусь к незнакомцам и всегда жду от них худшего'],
        6: ['Однажды выбрав цель, я становлюсь одержимым ею в ущерб всему прочему в своей жизни'],
    }

    selection_mechanics(background_personality_traits_list,
                        background_ideals_list,
                        background_bonds_list,
                        background_flaws_list)


def charlatan_background():  # ШАРЛАТАН
    pass


def criminal_background():  # ПРЕСТУПНИК
    pass


def artist_background():  # АРТИСТ
    pass


def folk_hero_background():  # НАРОДНЫЙ ГЕРОЙ
    pass


def guild_craftsmen_background():  # ГИЛЬДЕЙСКИЙ РЕМЕСЛЕННИК
    pass


def hermit_background():  # ОТШЕЛЬНИК
    pass


def noble_background():  # БЛАГОРОДНЫЙ
    pass


def aliens_background():  # ЧУЖЕЗЕМЕЦ
    pass


def sage_background():  # МУДРЕЦ
    pass


def sailor_background():  # МОРЯК
    pass


def soldier_background():  # СОЛДАТ
    pass


def throwaway_background():  # БЕСПРИЗОРНИК
    pass


def selection_mechanics(background_personality_traits_list,
                        background_ideals_list,
                        background_bonds_list,
                        background_flaws_list):
    print('Шаг 5.1: Выбор черты характера')
    for number, name in background_personality_traits_list.items():
        print(' {num:^5} |    {name} '.format(num=number, name=name[0]))
    print()

    user_input_personality_traits = int(input('Введите номер черты характера: '))

    while user_input_personality_traits not in background_personality_traits_list:
        print('Такой черты характера нет')
        user_input_personality_traits = int(input("Введите номер черты характера: "))
    else:
        print('Вы выбрали черту характера', background_personality_traits_list[user_input_personality_traits][0], '\n')
        name_background_personality_traits = background_personality_traits_list[user_input_personality_traits][0]
        player.personality_traits = name_background_personality_traits

    #     ++++++++++++++++++++++++++++++

    print('Шаг 5.2: Выбор идеала')
    for number, name in background_ideals_list.items():
        print(' {num:^5} |    {name} '.format(num=number, name=name[0]))
    print()

    user_input_ideals = int(input('Введите номер идеала: '))

    while user_input_ideals not in background_ideals_list:
        print('Такого идеала нет')
        user_input_ideals = int(input("Введите номер идеала: "))
    else:
        print('Вы выбрали идеал', background_ideals_list[user_input_ideals][0], '\n')
        name_background_ideals = background_ideals_list[user_input_ideals][0]
        player.ideals = name_background_ideals

    #     ++++++++++++++++++++++++++++++

    print('Шаг 5.3: Выбор привязанности')
    for number, name in background_bonds_list.items():
        print(' {num:^5} |    {name} '.format(num=number, name=name[0]))
    print()

    user_input_bonds = int(input('Введите номер привязанности: '))

    while user_input_bonds not in background_bonds_list:
        print('Такой привязанности нет')
        user_input_bonds = int(input("Введите номер привязанности: "))
    else:
        print('Вы выбрали привязанность', background_bonds_list[user_input_bonds][0], '\n')
        name_background_bonds = background_bonds_list[user_input_bonds][0]
        player.bonds = name_background_bonds

    #     ++++++++++++++++++++++++++++++

    print('Шаг 5.4: Выбор слабости')
    for number, name in background_flaws_list.items():
        print(' {num:^5} |    {name} '.format(num=number, name=name[0]))
    print()

    user_input_flaws = int(input('Введите номер слабости: '))

    while user_input_flaws not in background_flaws_list:
        print('Такой слабости нет')
        user_input_flaws = int(input("Введите номер слабости: "))
    else:
        print('Вы выбрали слабость', background_flaws_list[user_input_flaws][0], '\n')
        name_background_flaws = background_flaws_list[user_input_flaws][0]
        player.flaws = name_background_flaws

    return background_personality_traits_list, background_ideals_list, background_bonds_list, background_flaws_list

