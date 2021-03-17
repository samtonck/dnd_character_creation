from termcolor import colored
import game_race
import game_class
import game_background
import player


def line():
    print(colored('{txt:*^119}'.format(txt='*'), 'blue'))


def mod_saving(saving_throws_strength, saving_throws_dexterity, saving_throws_constitution, saving_throws_intelligence,
               saving_throws_wisdom, saving_throws_charisma):
    player.saving_throws_strength = (player.strength - 10) // 2  # модификатор сила
    player.saving_throws_dexterity = (player.dexterity - 10) // 2  # модификатор ловкость
    player.saving_throws_constitution = (player.constitution - 10) // 2  # модификатор телосложение
    player.saving_throws_intelligence = (player.intelligence - 10) // 2  # модификатор интеллект
    player.saving_throws_wisdom = (player.wisdom - 10) // 2  # модификатор мудрость
    player.saving_throws_charisma = (player.charisma - 10) // 2  # модификатор харизма
    return (saving_throws_strength, saving_throws_dexterity, saving_throws_constitution, saving_throws_intelligence,
            saving_throws_wisdom, saving_throws_charisma)


def mod_stat(mod_strength, mod_dexterity, mod_constitution, mod_intelligence, mod_wisdom, mod_charisma):
    player.mod_strength = (player.strength - 10) // 2  # модификатор сила
    player.mod_dexterity = (player.dexterity - 10) // 2  # модификатор ловкость
    player.mod_constitution = (player.constitution - 10) // 2  # модификатор телосложение
    player.mod_intelligence = (player.intelligence - 10) // 2  # модификатор интеллект
    player.mod_wisdom = (player.wisdom - 10) // 2  # модификатор мудрость
    player.mod_charisma = (player.charisma - 10) // 2  # модификатор харизма
    return mod_strength, mod_dexterity, mod_constitution, mod_intelligence, mod_wisdom, mod_charisma


def mod_skill(acrobatics, perception, athletics, investigation, survival, performance, intimidation, history,
              sleight_of_hand, arcana, medicine, deception, nature, insight, religion, stealth, persuasion,
              animal_handling):
    player.acrobatics = (player.dexterity - 10) // 2  # акробатика
    player.perception = (player.intelligence - 10) // 2  # анализ
    player.athletics = (player.strength - 10) // 2  # атлетика
    player.investigation = (player.wisdom - 10) // 2  # внимательность
    player.survival = (player.wisdom - 10) // 2  # выживание
    player.performance = (player.charisma - 10) // 2  # выступление
    player.intimidation = (player.charisma - 10) // 2  # запугивание
    player.history = (player.intelligence - 10) // 2  # история
    player.sleight_of_hand = (player.dexterity - 10) // 2  # ловкость рук
    player.arcana = (player.intelligence - 10) // 2  # магия
    player.medicine = (player.wisdom - 10) // 2  # медицина
    player.deception = (player.charisma - 10) // 2  # обман
    player.nature = (player.intelligence - 10) // 2  # природа
    player.insight = (player.wisdom - 10) // 2  # проницательность
    player.religion = (player.intelligence - 10) // 2  # религия
    player.stealth = (player.dexterity - 10) // 2  # скрытность
    player.persuasion = (player.charisma - 10) // 2  # убеждение
    player.animal_handling = (player.wisdom - 10) // 2  # уход за животными
    return (acrobatics, perception, athletics, investigation, survival, performance, intimidation, history,
            sleight_of_hand, arcana, medicine, deception, nature, insight, religion, stealth, persuasion,
            animal_handling)


result_race = game_race.input_race()
result_class = game_class.input_class()
result_background = game_background.input_background()

print(colored('Итого:', color='cyan'))

line()
print(colored('имя игрока', color='cyan'), '=', colored(player.name_player, color='yellow'))
line()
print(colored('имя персонажа', color='cyan'), '=', colored(player.name, color='yellow'))
print(colored('пол персонажа', color='cyan'), '=', colored(player.game_gender, color='yellow'))
print(colored('возраст персонажа', color='cyan'), '=', colored(player.age, color='yellow'))
print(colored('рост персонажа', color='cyan'), '=', colored(player.height, color='yellow'))
print(colored('вес персонажа', color='cyan'), '=', colored(player.weight, color='yellow'))
line()
print(colored('раса', color='cyan'), '=', colored(player.race, color='yellow'))
print(colored('класс', color='cyan'), '=', colored(player.game_class, color='yellow'))
print(colored('предыстория', color='cyan'), '=', colored(player.background, color='yellow'))
print(colored('мировоззрение', color='cyan'), '=', colored(player.alignment, color='yellow'))
line()
print(colored('призвание/гильдия/судьбоносное происшествие', color='cyan'), '=', colored(player.like_mechanics,
                                                                                         color='yellow'))
print(colored('черты характера', color='cyan'), '=', colored(player.personality_traits, color='yellow'))
print(colored('идеалы', color='cyan'), '=', colored(player.ideals, color='yellow'))
print(colored('привязанности', color='cyan'), '=', colored(player.bonds, color='yellow'))
print(colored('слабости', color='cyan'), '=', colored(player.flaws, color='yellow'))
line()
print(colored('уровень', color='cyan'), '=', colored(player.level, color='yellow'))
print(colored('опыт', color='cyan'), '=', colored(player.experience_point, color='yellow'))
print(colored('бонус мастерства', color='cyan'), '=', colored(player.proficiency_bonus, color='yellow'))
line()
print(colored('сила', color='cyan'), '=', colored(player.strength, color='yellow'))
print(colored('ловкость', color='cyan'), '=', colored(player.dexterity, color='yellow'))
print(colored('телосложение', color='cyan'), '=', colored(player.constitution, color='yellow'))
print(colored('интеллект', color='cyan'), '=', colored(player.intelligence, color='yellow'))
print(colored('мудрость', color='cyan'), '=', colored(player.wisdom, color='yellow'))
print(colored('харизма', color='cyan'), '=', colored(player.charisma, color='yellow'))
line()

mod_saving(player.mod_strength, player.mod_dexterity, player.mod_constitution,
           player.mod_intelligence, player.mod_wisdom, player.mod_charisma)

mod_stat(player.saving_throws_strength, player.saving_throws_dexterity, player.saving_throws_constitution,
         player.saving_throws_intelligence, player.saving_throws_wisdom, player.saving_throws_charisma)

mod_skill(player.acrobatics, player.perception, player.athletics, player.investigation, player.survival,
          player.performance, player.intimidation, player.history, player.sleight_of_hand, player.arcana,
          player.medicine, player.deception, player.nature, player.insight, player.religion, player.stealth,
          player.persuasion, player.animal_handling)

print(colored('модификатор сила', color='cyan'), '=', colored(player.mod_strength, color='yellow'))
print(colored('модификатор ловкость', color='cyan'), '=', colored(player.mod_dexterity, color='yellow'))
print(colored('модификатор телосложение', color='cyan'), '=', colored(player.mod_constitution, color='yellow'))
print(colored('модификатор интеллект', color='cyan'), '=', colored(player.mod_intelligence, color='yellow'))
print(colored('модификатор мудрость', color='cyan'), '=', colored(player.mod_wisdom, color='yellow'))
print(colored('модификатор харизма', color='cyan'), '=', colored(player.mod_charisma, color='yellow'))
line()

if player.check_saving_throws_strength is True:
    player.saving_throws_strength += player.proficiency_bonus
    print(colored('знание спас броска сила', color='cyan'), '=',
          colored(player.check_saving_throws_strength, color='yellow'))
if player.check_saving_throws_dexterity is True:
    player.saving_throws_dexterity += player.proficiency_bonus
    print(colored('знание спас броска ловкость', color='cyan'), '=',
          colored(player.check_saving_throws_dexterity, color='yellow'))
if player.check_saving_throws_constitution is True:
    player.saving_throws_constitution += player.proficiency_bonus
    print(colored('знание спас броска телосложение', color='cyan'), '=',
          colored(player.check_saving_throws_constitution, color='yellow'))
if player.check_saving_throws_intelligence is True:
    player.saving_throws_intelligence += player.proficiency_bonus
    print(colored('знание спас броска интеллект', color='cyan'), '=',
          colored(player.check_saving_throws_intelligence, color='yellow'))
if player.check_saving_throws_wisdom is True:
    player.saving_throws_wisdom += player.proficiency_bonus
    print(colored('знание спас броска мудрость', color='cyan'), '=',
          colored(player.check_saving_throws_wisdom, color='yellow'))
if player.check_saving_throws_charisma is True:
    player.saving_throws_charisma += player.proficiency_bonus
    print(colored('знание спас броска харизма', color='cyan'), '=',
          colored(player.check_saving_throws_charisma, color='yellow'))
line()
print(colored('спас бросок сила', color='cyan'), '=', colored(player.saving_throws_strength, color='yellow'))
print(colored('спас бросок ловкость', color='cyan'), '=', colored(player.saving_throws_dexterity, color='yellow'))
print(colored('спас бросок телосложение', color='cyan'), '=', colored(player.saving_throws_constitution,
                                                                      color='yellow'))
print(colored('спас бросок интеллект', color='cyan'), '=', colored(player.saving_throws_intelligence, color='yellow'))
print(colored('спас бросок мудрость', color='cyan'), '=', colored(player.saving_throws_wisdom, color='yellow'))
print(colored('спас бросок харизма', color='cyan'), '=', colored(player.saving_throws_charisma, color='yellow'))
line()
if player.check_acrobatics is True:
    player.acrobatics += player.proficiency_bonus
    print(colored('знание акробатика', color='cyan'), '=', colored(player.check_acrobatics, color='yellow'))
if player.check_perception is True:
    player.perception += player.proficiency_bonus
    print(colored('знание анализ', color='cyan'), '=', colored(player.check_perception, color='yellow'))
if player.check_athletics is True:
    player.athletics += player.proficiency_bonus
    print(colored('знание атлетика', color='cyan'), '=', colored(player.check_athletics, color='yellow'))
if player.check_investigation is True:
    player.investigation += player.proficiency_bonus
    print(colored('знание внимательность', color='cyan'), '=', colored(player.check_investigation, color='yellow'))
if player.check_survival is True:
    player.survival += player.proficiency_bonus
    print(colored('знание выживание', color='cyan'), '=', colored(player.check_survival, color='yellow'))
if player.check_performance is True:
    player.performance += player.proficiency_bonus
    print(colored('знание выступление', color='cyan'), '=', colored(player.check_performance, color='yellow'))
if player.check_intimidation is True:
    player.intimidation += player.proficiency_bonus
    print(colored('знание запугивание', color='cyan'), '=', colored(player.check_intimidation, color='yellow'))
if player.check_history is True:
    player.history += player.proficiency_bonus
    print(colored('знание история', color='cyan'), '=', colored(player.check_history, color='yellow'))
if player.check_sleight_of_hand is True:
    player.sleight_of_hand += player.proficiency_bonus
    print(colored('знание ловкость рук', color='cyan'), '=', colored(player.check_sleight_of_hand, color='yellow'))
if player.check_arcana is True:
    player.arcana += player.proficiency_bonus
    print(colored('знание магия', color='cyan'), '=', colored(player.check_arcana, color='yellow'))
if player.check_medicine is True:
    player.medicine += player.proficiency_bonus
    print(colored('знание медицина', color='cyan'), '=', colored(player.check_medicine, color='yellow'))
if player.check_deception is True:
    player.deception += player.proficiency_bonus
    print(colored('знание обман', color='cyan'), '=', colored(player.check_deception, color='yellow'))
if player.check_nature is True:
    player.nature += player.proficiency_bonus
    print(colored('знание природа', color='cyan'), '=', colored(player.check_nature, color='yellow'))
if player.check_insight is True:
    player.insight += player.proficiency_bonus
    print(colored('знание проницательность', color='cyan'), '=', colored(player.check_insight, color='yellow'))
if player.check_religion is True:
    player.religion += player.proficiency_bonus
    print(colored('знание религия', color='cyan'), '=', colored(player.check_religion, color='yellow'))
if player.check_stealth is True:
    player.stealth += player.proficiency_bonus
    print(colored('знание скрытность', color='cyan'), '=', colored(player.check_stealth, color='yellow'))
if player.check_persuasion is True:
    player.persuasion += player.proficiency_bonus
    print(colored('знание убеждение', color='cyan'), '=', colored(player.check_persuasion, color='yellow'))
if player.check_animal_handling is True:
    player.animal_handling += player.proficiency_bonus
    print(colored('знание уход за животными', color='cyan'), '=', colored(player.check_animal_handling, color='yellow'))
line()
print(colored('акробатика', color='cyan'), '=', colored(player.acrobatics, color='yellow'))
print(colored('анализ', color='cyan'), '=', colored(player.perception, color='yellow'))
print(colored('атлетика', color='cyan'), '=', colored(player.athletics, color='yellow'))
print(colored('внимательность', color='cyan'), '=', colored(player.investigation, color='yellow'))
print(colored('выживание', color='cyan'), '=', colored(player.survival, color='yellow'))
print(colored('выступление', color='cyan'), '=', colored(player.performance, color='yellow'))
print(colored('запугивание', color='cyan'), '=', colored(player.intimidation, color='yellow'))
print(colored('история', color='cyan'), '=', colored(player.history, color='yellow'))
print(colored('ловкость рук', color='cyan'), '=', colored(player.sleight_of_hand, color='yellow'))
print(colored('магия', color='cyan'), '=', colored(player.arcana, color='yellow'))
print(colored('медицина', color='cyan'), '=', colored(player.medicine, color='yellow'))
print(colored('обман', color='cyan'), '=', colored(player.deception, color='yellow'))
print(colored('природа', color='cyan'), '=', colored(player.nature, color='yellow'))
print(colored('проницательность', color='cyan'), '=', colored(player.insight, color='yellow'))
print(colored('религия', color='cyan'), '=', colored(player.religion, color='yellow'))
print(colored('скрытность', color='cyan'), '=', colored(player.stealth, color='yellow'))
print(colored('убеждение', color='cyan'), '=', colored(player.persuasion, color='yellow'))
print(colored('уход за животными', color='cyan'), '=', colored(player.animal_handling, color='yellow'))
line()

player.passive_wisdom = 10 + player.mod_wisdom
print(colored('пассивная мудрость (внимательность)', color='cyan'), '=', colored(player.passive_wisdom, color='yellow'))
line()

player.armor_class = 10 + player.mod_dexterity
print(colored('КД (класс доспеха)', color='cyan'), '=', colored(player.armor_class, color='yellow'))

player.initiative = player.mod_dexterity
print(colored('инициатива', color='cyan'), '=', colored(player.initiative, color='yellow'))
print(colored('скорость', color='cyan'), '=', colored(player.speed, color='yellow'))
line()
print(colored('максимальное кол-во очков жизни', color='cyan'), '=', colored(player.hit_point_maximum, color='yellow'))
print(colored('кубик жизни', color='cyan'), '=', colored(player.hit_dise, color='yellow'))
line()
print(colored('темное зрение', color='cyan'), '=', colored(player.dark_vision, color='yellow'))
print(colored('языки', color='cyan'), '=', colored(player.language, color='yellow'))
line()
print(colored('другие умения', color='cyan'), '=', colored(player.other, color='yellow'))
print(colored('навыки', color='cyan'), '=', colored(player.skills, color='yellow'))
print(colored('снаряжение', color='cyan'), '=', colored(player.equipment, color='yellow'))
line()
