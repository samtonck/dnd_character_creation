from termcolor import colored


print(colored('{txt:*^119}'.format(txt='*'), 'red'))
print(colored("""
                                                         |--__
                                                         |
                                                         X
                                                |-___   / \       |--__
                                                |      =====      |
                                                X      | .:|      X
                                               / \     | O |     / \\
                                              =====   |:  . |   =====
                                              |.: |__| .   : |__| :.|
                                              |  :|. :  ...   : |.  |
                                      __   __W| .    .  ||| .      :|W__  --
                                    -- __  W  WWWW______"_"______WWWW   W -----  --
                                -  -     ___  ---    ____     ____----       --__  -
                                    --__    --    --__     -___        __-   _
""", 'red'))
print(colored('{txt:*^119}'.format(txt='*'), 'red'))
print(colored('{txt:*^119}'.format(txt='*'), 'blue'))
print(colored("""
                                                     Привет!
                                                    
                    Это приложение по созданию листа персонажа для игры Dungeons & Dragons. 
                    Ниже будут появляться инструкции, следуй им и у тебя будет самый топовый персонаж
""", 'blue'))
print(colored('{txt:*^119}'.format(txt='*'), 'blue'))
print('{txt:*^119}\n'.format(txt='*'))
name_player = input('Шаг 1: Для начала давай познакомимся! Введите ваше имя: ')  # имя игрока
print()


def input_gender():
    print('Шаг 2: За персонажа какого пола вы будете играть: ')
    gender = {
        1: ['Мужчина (Man)'],
        2: ['Женщина (Woman)']
    }
    for number, gender_name in gender.items():
        print(' {num:^5} |    {name} '.format(num=number, name=gender_name[0]))
    user_input_gender = int(input('Введите номер пола: '))

    while user_input_gender not in gender:
        print('Такого пола нет')
        user_input_gender = int(input("Введите номер пола: "))
    else:
        print('Вы выбрали пол', gender[user_input_gender][0], '\n')
        name_gender = gender[user_input_gender][0]
        return name_gender


def input_level():
    print('Шаг 3: За персонажа какого уровня вы будете играть: ')
    user_input_level = int(input('Введите номер уровня от 1 до 20: '))

    while 20 < user_input_level < 1:
        print('Такого уровня нет')
        user_input_level = int(input("Введите номер уровня от 1 до 20: "))
    else:
        print('Вы выбрали уровень', user_input_level, '\n')
        name_level = user_input_level
        return name_level


name = ''  # имя персонажа
game_gender = input_gender()  # пол персонажа
age = ''  # возраст персонажа
height = ''  # рост персонажа
weight = ''  # вес персонажа

race = ''  # раса
game_class = ''  # класс
background = ''  # предыстория
alignment = ''  # мировоззрение

like_mechanics = ''  # призвание/гильдия/судьбоносное происшествие
personality_traits = ''  # черты характера
ideals = ''  # идеалы
bonds = ''  # привязанности
flaws = ''  # слабости

level = input_level()  # уровень
experience_point = 0  # опыт
proficiency_bonus = 0  # бонус мастерства

if level == 1:
    experience_point = 0
    proficiency_bonus = 2
elif level == 2:
    experience_point = 300
    proficiency_bonus = 2
elif level == 3:
    experience_point = 900
    proficiency_bonus = 2
elif level == 4:
    experience_point = 2700
    proficiency_bonus = 2
elif level == 5:
    experience_point = 6500
    proficiency_bonus = 3
elif level == 6:
    experience_point = 14000
    proficiency_bonus = 3
elif level == 7:
    experience_point = 23000
    proficiency_bonus = 3
elif level == 8:
    experience_point = 34000
    proficiency_bonus = 3
elif level == 9:
    experience_point = 48000
    proficiency_bonus = 4
elif level == 10:
    experience_point = 64000
    proficiency_bonus = 4
elif level == 11:
    experience_point = 85000
    proficiency_bonus = 4
elif level == 12:
    experience_point = 100000
    proficiency_bonus = 4
elif level == 13:
    experience_point = 120000
    proficiency_bonus = 5
elif level == 14:
    experience_point = 140000
    proficiency_bonus = 5
elif level == 15:
    experience_point = 165000
    proficiency_bonus = 5
elif level == 16:
    experience_point = 195000
    proficiency_bonus = 5
elif level == 17:
    experience_point = 225000
    proficiency_bonus = 6
elif level == 18:
    experience_point = 265000
    proficiency_bonus = 6
elif level == 19:
    experience_point = 305000
    proficiency_bonus = 6
elif level == 20:
    experience_point = 355000
    proficiency_bonus = 6

strength = 0  # сила
dexterity = 0  # ловкость
constitution = 0  # телосложение
intelligence = 0  # интеллект
wisdom = 0  # мудрость
charisma = 0  # харизма

mod_strength = 0  # модификатор сила
mod_dexterity = 0  # модификатор ловкость
mod_constitution = 0  # модификатор телосложение
mod_intelligence = 0  # модификатор интеллект
mod_wisdom = 0  # модификатор мудрость
mod_charisma = 0  # модификатор харизма

check_saving_throws_strength = False  # знание спас бросок сила
check_saving_throws_dexterity = False  # знание  спас бросок ловкость
check_saving_throws_constitution = False  # знание  спас бросок телосложение
check_saving_throws_intelligence = False  # знание  спас бросок интеллект
check_saving_throws_wisdom = False  # знание  спас бросок мудрость
check_saving_throws_charisma = False  # знание  спас бросок харизма

saving_throws_strength = mod_strength  # спас бросок сила
saving_throws_dexterity = mod_dexterity  # спас бросок ловкость
saving_throws_constitution = mod_constitution  # спас бросок телосложение
saving_throws_intelligence = mod_intelligence  # спас бросок интеллект
saving_throws_wisdom = mod_wisdom  # спас бросок мудрость
saving_throws_charisma = mod_charisma  # спас бросок харизма

check_acrobatics = False  # знание акробатика
check_perception = False  # знание анализ
check_athletics = False  # знание атлетика
check_investigation = False  # знание внимательность
check_survival = False  # знание выживание
check_performance = False  # знание выступление
check_intimidation = False  # знание запугивание
check_history = False  # знание история
check_sleight_of_hand = False  # знание ловкость рук
check_arcana = False  # знание магия
check_medicine = False  # знание медицина
check_deception = False  # знание обман
check_nature = False  # знание природа
check_insight = False  # знание проницательность
check_religion = False  # знание религия
check_stealth = False  # знание скрытность
check_persuasion = False  # знание убеждение
check_animal_handling = False  # знание уход за животными

acrobatics = mod_dexterity  # акробатика
perception = mod_intelligence  # анализ
athletics = mod_strength  # атлетика
investigation = mod_wisdom  # внимательность
survival = mod_wisdom  # выживание
performance = mod_charisma  # выступление
intimidation = mod_charisma  # запугивание
history = mod_intelligence  # история
sleight_of_hand = mod_dexterity  # ловкость рук
arcana = mod_intelligence  # магия
medicine = mod_wisdom  # медицина
deception = mod_charisma  # обман
nature = mod_intelligence  # природа
insight = mod_wisdom  # проницательность
religion = mod_intelligence  # религия
stealth = mod_dexterity  # скрытность
persuasion = mod_charisma  # убеждение
animal_handling = mod_wisdom  # уход за животными

passive_wisdom = 10 + mod_wisdom  # пассивная мудрость (внимательность)

armor_class = 0  # КД (класс доспеха)
initiative = dexterity  # инициатива
speed = 0  # скорость

hit_point_maximum = 0  # максимальное кол-во очков жизни
hit_dise = ''  # кубик жизни

dark_vision = ''  # темное зрение
language = ''  # языки
other = ''  # другие умения
skills = ''  # навыки
equipment = ''  # снаряжение
