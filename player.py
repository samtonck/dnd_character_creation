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


name = ''  # имя персонажа
game_gender = input_gender()  # пол персонажа
age = ''  # возраст персонажа
height = ''  # рост персонажа
weight = ''  # вес персонажа

race = ''  # раса
game_class = ''  # класс
background = ''  # предыстория
alignment = ''  # мировоззрение

personality_traits = ''  # черты характера
ideals = ''  # идеалы
bonds = ''  # привязанности
flaws = ''  # слабости

level = 1  # уровень по умолчанию 1
experience_point = 0  # опыт
proficiency_bonus = 0  # бонус мастерства

strength = 0  # сила
dexterity = 0  # ловкость
constitution = 0  # телосложение
intelligence = 0  # интеллект
wisdom = 0  # мудрость
charisma = 0  # харизма

mod_strength = (strength - 10) // 2  # модификатор сила
mod_dexterity = (dexterity - 10) // 2  # модификатор ловкость
mod_constitution = (constitution - 10) // 2  # модификатор телосложение
mod_intelligence = (intelligence - 10) // 2  # модификатор интеллект
mod_wisdom = (wisdom - 10) // 2  # модификатор мудрость
mod_charisma = (charisma - 10) // 2  # модификатор харизма

saving_throws_strength = 0  # спас бросок сила
saving_throws_dexterity = 0  # спас бросок ловкость
saving_throws_constitution = 0  # спас бросок телосложение
saving_throws_intelligence = 0  # спас бросок интеллект
saving_throws_wisdom = 0  # спас бросок мудрость
saving_throws_charisma = 0  # спас бросок харизма

check_saving_throws_strength = False  # знание спас бросок сила
check_saving_throws_dexterity = False  # знание  спас бросок ловкость
check_saving_throws_constitution = False  # знание  спас бросок телосложение
check_saving_throws_intelligence = False  # знание  спас бросок интеллект
check_saving_throws_wisdom = False  # знание  спас бросок мудрость
check_saving_throws_charisma = False  # знание  спас бросок харизма

if check_saving_throws_strength is True:
    saving_throws_strength += proficiency_bonus
if check_saving_throws_dexterity is True:
    saving_throws_dexterity += proficiency_bonus
if check_saving_throws_constitution is True:
    saving_throws_constitution += proficiency_bonus
if check_saving_throws_intelligence is True:
    saving_throws_intelligence += proficiency_bonus
if check_saving_throws_wisdom is True:
    saving_throws_wisdom += proficiency_bonus
if check_saving_throws_charisma is True:
    saving_throws_charisma += proficiency_bonus

acrobatics = 0  # акробатика
perception = 0  # анализ
athletics = 0  # атлетика
investigation = 0  # внимательность
survival = 0  # выживание
performance = 0  # выступление
intimidation = 0  # запугивание
history = 0  # история
sleight_of_hand = 0  # ловкость рук
arcana = 0  # магия
medicine = 0  # медицина
deception = 0  # обман
nature = 0  # природа
insight = 0  # проницательность
religion = 0  # религия
stealth = 0  # скрытность
persuasion = 0  # убеждение
animal_handling = 0  # уход за животными

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

if check_acrobatics is True:
    acrobatics += proficiency_bonus
if check_perception is True:
    perception += proficiency_bonus
if check_athletics is True:
    athletics += proficiency_bonus
if check_investigation is True:
    investigation += proficiency_bonus
if check_survival is True:
    survival += proficiency_bonus
if check_performance is True:
    performance += proficiency_bonus
if check_intimidation is True:
    intimidation += proficiency_bonus
if check_history is True:
    history += proficiency_bonus
if check_sleight_of_hand is True:
    sleight_of_hand += proficiency_bonus
if check_arcana is True:
    arcana += proficiency_bonus
if check_medicine is True:
    medicine += proficiency_bonus
if check_deception is True:
    deception += proficiency_bonus
if check_nature is True:
    nature += proficiency_bonus
if check_insight is True:
    insight += proficiency_bonus
if check_religion is True:
    religion += proficiency_bonus
if check_stealth is True:
    stealth += proficiency_bonus
if check_persuasion is True:
    persuasion += proficiency_bonus
if check_animal_handling is True:
    animal_handling += proficiency_bonus

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
