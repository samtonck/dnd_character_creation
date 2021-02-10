
name = ''  # имя персонажа
height = ''  # рост персонажа
weight = ''  # вес персонажа
age = ''  # возраст персонажа

game_class = ''  # класс
level = 1  # уровень по умолчанию 1
race = ''  # расса
background = ''  # предыстория
alignment = ''  # мировоззрение
name_player = input('Шаг 1: Введите ваше имя: ')  # имя игрока
experience_point = 0  # опыт

personality_traits = ''  # черты характера
ideals = ''  # идеалы
bonds = ''  # привязанности
flaws = ''  # слабости

strength = 0  # сила
dexterity = 0  # ловкость
constitution = 0  # телосложение
intelligence = 0  # интелект
wisdom = 0  # мудрость
charisma = 0  # харизма

proficiency_bonus = 0  # бонус мастерства

mod_strength = (strength - 10) // 2  # модификатор сила
mod_dexterity = (dexterity - 10) // 2  # модификатор ловкость
mod_constitution = (constitution - 10) // 2  # модификатор телосложение
mod_intelligence = (intelligence - 10) // 2  # модификатор интелект
mod_wisdom = (wisdom - 10) // 2  # модификатор мудрость
mod_charisma = (charisma - 10) // 2  # модификатор харизма

saving_throws_strength = 0  # спас бросок сила
saving_throws_dexterity = 0  # спас бросок ловкость
saving_throws_constitution = 0  # спас бросок телосложение
saving_throws_intelligence = 0  # спас бросок интелект
saving_throws_wisdom = 0  # спас бросок мудрость
saving_throws_charisma = 0  # спас бросок харизма

check_saving_throws_strength = False  # спас бросок сила
check_saving_throws_dexterity = False  # спас бросок ловкость
check_saving_throws_constitution = False  # спас бросок телосложение
check_saving_throws_intelligence = False  # спас бросок интелект
check_saving_throws_wisdom = False  # спас бросок мудрость
check_saving_throws_charisma = False  # спас бросок харизма

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

acrobatics = 0  #
animal_handling = 0  #
arcana = 0  #
athletics = 0  #
deception = 0  #
history = 0  #
insight = 0  #
intimidation = 0  #
investigation = 0  #
medicine = 0  #
nature = 0  #
perception = 0  #
performance = 0  #
persuasion = 0  #
religion = 0  #
sleight_of_hand = 0  #
stealth = 0  #
survival = 0  #

passive_wisdom = 10 + mod_wisdom  # пассивная мудрость (внимательность)

armor_class = 0  # КД (класс доспеха)
initiative = dexterity  # инициатива
speed = 0  # скорость

hit_point_maximum = 0  # максимальное кол-во очков жизни
hit_dise = ''  # кубик жизни

dark_vision = ''  # темное зрение
language = ''  # языки
other = ''  # другие умения
