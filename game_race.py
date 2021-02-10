

def input_race():
    print('Шаг 1: Выбор расы')
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
    return name_race


game_race = {
    1: ['Гном (Gnome)'],
    2: ['Дварф (Dwarf)'],
    3: ['Драконорожденный (Dragonborn)'],
    4: ['Полуорк (Half-orc)'],
    5: ['Полурослик (Halfling)'],
    6: ['Полуэльф (Half-elf)'],
    7: ['Тифлинг (Tiefling)'],
    8: ['Человек (Human)'],
    9: ['Эльф (Elf)']
}
