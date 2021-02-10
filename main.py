import random as random
from termcolor import cprint
import game_race
import game_class
import game_background


print('\nПривет!\n\nЭто приложение по созданию листа персонажа\n')

result_race = game_race.input_race()
result_class = game_class.input_class()
result_background = game_background.input_background()


cprint('Итого:', color='green')
cprint('РАСА = {}'.format(result_race), color='yellow')
cprint('КЛАСС = {}'.format(result_class), color='yellow')
cprint('ПРОИСХОЖДЕНИЕ = {}'.format(result_background), color='yellow')
