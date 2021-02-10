

class Player:  # игрок

    def __init__(self):
        self.name = ''  # имя персонажа
        self.height = ''  # рост персонажа
        self.weight = ''  # вес персонажа

        self.game_class = ''  # класс
        self.level = 1  # уровень по умолчанию 1
        self.race = ''  # расса
        self.background = ''  # предыстория
        self.alignment = ''  # мировоззрение
        self.name_player = ''  # имя игрока
        self.experience_point = 0  # опыт

        self.personality_traits = ''  # черты характера
        self.ideals = ''  # идеалы
        self.bonds = ''  # привязанности
        self.flaws = ''  # слабости

        self.strength = 0  # сила
        self.dexterity = 0  # ловкость
        self.constitution = 0  # телосложение
        self.intelligence = 0  # интелект
        self.wisdom = 0  # мудрость
        self.charisma = 0  # харизма

        self.proficiency_bonus = 0  # бонус мастерства

        self.mod_strength = (self.strength - 10) // 2  # модификатор сила
        self.mod_dexterity = (self.dexterity - 10) // 2  # модификатор ловкость
        self.mod_constitution = (self.constitution - 10) // 2  # модификатор телосложение
        self.mod_intelligence = (self.intelligence - 10) // 2  # модификатор интелект
        self.mod_wisdom = (self.wisdom - 10) // 2  # модификатор мудрость
        self.mod_charisma = (self.charisma - 10) // 2  # модификатор харизма

        self.saving_throws_strength = 0  # спас бросок сила
        self.saving_throws_dexterity = 0  # спас бросок ловкость
        self.saving_throws_constitution = 0  # спас бросок телосложение
        self.saving_throws_intelligence = 0  # спас бросок интелект
        self.saving_throws_wisdom = 0  # спас бросок мудрость
        self.saving_throws_charisma = 0  # спас бросок харизма

        self.acrobatics = 0  #
        self.animal_handling = 0  #
        self.arcana = 0  #
        self.athletics = 0  #
        self.deception = 0  #
        self.history = 0  #
        self.insight = 0  #
        self.intimidation = 0  #
        self.investigation = 0  #
        self.medicine = 0  #
        self.nature = 0  #
        self.perception = 0  #
        self.performance = 0  #
        self.persuasion = 0  #
        self.religion = 0  #
        self.sleight_of_hand = 0  #
        self.stealth = 0  #
        self.survival = 0  #

        self.passive_wisdom = 10 + self.mod_wisdom  # пассивная мудрость (внимательность)

        self.armor_class = 0  # КД (класс доспеха)
        self.initiative = self.dexterity  # инициатива
        self.speed = 0  # скорость

        self.hit_point_maximum = 0  # максимальное кол-во очков жизни
        self.hit_dise = ''  # кубик жизни

