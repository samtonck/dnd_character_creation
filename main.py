from termcolor import cprint
import game_race
import game_class
import game_background
import player


print('\nПривет!\n\nЭто приложение по созданию листа персонажа\n')

# player.name()
result_race = game_race.input_race()
result_class = game_class.input_class()
result_background = game_background.input_background()


cprint('Итого:', color='green')


cprint('имя игрока = {}'.format(player.name_player), color='yellow')

cprint('расса = {}'.format(player.race), color='yellow')
cprint('класс = {}'.format(player.game_class), color='yellow')
cprint('происхождение = {}'.format(result_background), color='yellow')

cprint('мировоззрение = {}'.format(player.alignment), color='yellow')
cprint('предыстория = {}'.format(player.background), color='yellow')

cprint('черты характера = {}'.format(player.personality_traits), color='yellow')
cprint('идеалы = {}'.format(player.ideals), color='yellow')
cprint('привязанности = {}'.format(player.bonds), color='yellow')
cprint('слабости = {}'.format(player.flaws), color='yellow')

cprint('имя персонажа = {}'.format(player.name), color='yellow')
cprint('возраст персонажа = {}'.format(player.age), color='yellow')
cprint('рост персонажа = {}'.format(player.height), color='yellow')
cprint('вес персонажа = {}'.format(player.weight), color='yellow')

cprint('уровень = {}'.format(player.level), color='yellow')
cprint('опыт = {}'.format(player.experience_point), color='yellow')

cprint('сила = {}'.format(player.strength), color='yellow')
cprint('ловкость = {}'.format(player.dexterity), color='yellow')
cprint('телосложение = {}'.format(player.constitution), color='yellow')
cprint('интелект = {}'.format(player.intelligence), color='yellow')
cprint('мудрость = {}'.format(player.wisdom), color='yellow')
cprint('харизма = {}'.format(player.charisma), color='yellow')

cprint('бонус мастерства = {}'.format(player.proficiency_bonus), color='yellow')

cprint('модификатор сила = {}'.format(player.mod_strength), color='yellow')
cprint('модификатор ловкость = {}'.format(player.mod_dexterity), color='yellow')
cprint('модификатор телосложение = {}'.format(player.mod_constitution), color='yellow')
cprint('модификатор интелект = {}'.format(player.mod_intelligence), color='yellow')
cprint('модификатор мудрость = {}'.format(player.mod_wisdom), color='yellow')
cprint('модификатор харизма = {}'.format(player.mod_charisma), color='yellow')

cprint('спас бросок сила = {}'.format(player.saving_throws_strength), color='yellow')
cprint('спас бросок ловкость = {}'.format(player.saving_throws_dexterity), color='yellow')
cprint('спас бросок телосложение = {}'.format(player.saving_throws_constitution), color='yellow')
cprint('спас бросок интелект = {}'.format(player.saving_throws_intelligence), color='yellow')
cprint('спас бросок мудрость = {}'.format(player.saving_throws_wisdom), color='yellow')
cprint('спас бросок харизма = {}'.format(player.saving_throws_charisma), color='yellow')

cprint('знание характеристики спас бросок сила = {}'.format(player.check_saving_throws_strength), color='yellow')
cprint('спас бросок ловкость = {}'.format(player.check_saving_throws_dexterity), color='yellow')
cprint('спас бросок телосложение = {}'.format(player.check_saving_throws_constitution), color='yellow')
cprint('спас бросок интелект = {}'.format(player.check_saving_throws_intelligence), color='yellow')
cprint('спас бросок мудрость = {}'.format(player.check_saving_throws_wisdom), color='yellow')
cprint('спас бросок харизма = {}'.format(player.check_saving_throws_charisma), color='yellow')

cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.acrobatics), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.animal_handling), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.arcana), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.athletics), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.deception), color='yellow')
cprint('история = {}'.format(player.history), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.insight), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.intimidation), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.investigation), color='yellow')
cprint('медицина = {}'.format(player.medicine), color='yellow')
cprint('природа = {}'.format(player.nature), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.perception), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.performance), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.persuasion), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.religion), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.sleight_of_hand), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.stealth), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(player.survival), color='yellow')

cprint('пассивная мудрость (внимательность) = {}'.format(player.passive_wisdom), color='yellow')

cprint('КД (класс доспеха) = {}'.format(player.armor_class), color='yellow')
cprint('инициатива = {}'.format(player.initiative), color='yellow')
cprint('скорость = {}'.format(player.speed), color='yellow')

cprint('максимальное кол-во очков жизни = {}'.format(player.hit_point_maximum), color='yellow')
cprint('кубик жизни = {}'.format(player.hit_dise), color='yellow')

cprint('темное зрение= {}'.format(player.dark_vision), color='yellow')
cprint('языки = {}'.format(player.language), color='yellow')
