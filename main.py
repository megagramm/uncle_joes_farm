import datetime
import random


def rprint(string):
    """Формирует вывод текста на экран по правому краю"""
    string_len = len(string)
    # print(f'\n{"="*(79-string_len-1)}{string:>79}\n')
    right_len=79-string_len
    print(f'\n{"="*19} {string:>59}\n')

class Animal:
    """Основной класс наших живых существ"""
    attributes = {
        'two_eyes': True,
        'two_ears': True,
        'spine': True,
        'blood': True
    }
    name = None
    weight = None
    sound = None
    __sex = None
    __birthday = None
    species_of_animals = None

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def get_sex(self):
        if self.__sex is None:
            # print(f"{self.name}: "
            #       f"Пол не определен. Оно требует называть себя ОНИ")
            return
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex

    def input_set_sex(self, intity=None):
        """Назначение пола через input()"""
        sex = input('Укажите пол (m, male, f, female): ').lower()
        if sex not in ['m', 'male', 'f', 'female']:
            print('Ваши значения не подходят:')
            return
        if sex == 'm':
            sex = 'male'
        if sex == 'f':
            sex = 'female'
        if intity == None:
            self.set_sex(sex)
        else:
            intity.set_sex(sex)

    def get_species_of_animals(self):
        if self.get_sex() == 'male':
            return self.species_of_animals[0]
        elif self.get_sex() == 'female':
            return self.species_of_animals[1]
        else:
            return

    def get_birthday(self):
        if self.__birthday is None:
            return "Не указано"
        return self.__birthday

    def set_birthday(self, date=None):
        if date is None:
            self.__birthday = datetime.datetime.now()
        else:
            self.__birthday = datetime.datetime.strptime(date, '%d-%m-%Y')

    def input_set_birthday(self):
        date = input('Введите дату рождения (ДД-ММ-ГГГГ): ')
        self.set_birthday(date)

    def say(self):
        """Что говорит животное"""
        if self.sound is None:
            print('Это существо не умеет издавать звуки')
        else:
            print(f'{self.name} ({self.get_species_of_animals()}): {self.sound}')

    def pet_the_animal(self):
        """Погладь животное"""
        self.say()
        print(f'Вы гладите животное. Все любят ласку. {self.name} радуется')

    def feed_the_animal(self, food_weight=0):
        if food_weight == 0:
            food_weight = round(self.weight*0.045,2)
        self.weight += round(food_weight*0.2, 2)
        print(f'{self.name} ест. Вес еды: {food_weight} кг. '
              f'Вес увеличился на {round(food_weight*0.2, 2)} кг и составил {self.weight} кг')

class Bird(Animal):
    """Подкласс живых существ"""
    bird_attr = {
        'beak': True,
        'wings': True,
        'feathers': True
    }

    def __init__(self, name, weight):
        self.attributes.update(self.bird_attr)
        self.name = name
        self.weight = weight

    def collect_eggs(self):
        """Собирать яйца"""
        if self.get_sex() != 'female':
            print(f'{self.name} ({self.get_species_of_animals()}): Можно собирать яйца только у самочки')
            return
        eggs = random.randint(0, 3)
        if eggs > 0:
            self.say()
            self.say()
            self.say()
            print(f'{self.name} ({self.species_of_animals[1].lower()}): снесла {eggs} яйца. Вы их забрали, она очень недовольна')
        else:
            print(f'{self.name}({self.species_of_animals[1]}): Не удалось собрать ни одного яйца. '
                  f'Либо {self.species_of_animals[1].lower()} перестала нестись, либо она их прячет')


class Mammal(Animal):
    """Подкласс живых существ"""
    mammal_attr = {
        'nose': True,
        'mouth': True,
        'teeth': True
    }

    def __init__(self, name: str, weight: float):
        self.attributes.update(self.mammal_attr)
        self.name = name
        self.weight = weight


class Goose(Bird):
    sound = 'Га-га-га'
    species_of_animals = ['Гусь', 'Гусыня']


class Cow(Mammal):
    sound = 'Муу-у'
    species_of_animals = ['Бык', 'Корова']

    def milking(self):
        if self.get_sex() == 'female':
            print(f'{self.name} ({self.get_species_of_animals()}): {self.get_species_of_animals()} подоена')
            return
        elif self.get_sex() == 'male':
            print(f'{self.name} ({self.get_species_of_animals()}): нельзя доить')
            return
        print(f'{self.name} нельзя доить')


class Sheep(Mammal):
    sound = 'Бе-е-е'
    species_of_animals = ['Баран', 'Овца']

    def shearing(self):
        """Стричь"""
        if self.get_species_of_animals() is not None:
            print(f'{self.name} ({self.get_species_of_animals()}): Стрижка произведена')
            return
        print(f'{self.name}: Стрижка произведена')




class Chicken(Bird):
    sound = 'Ку-ка-ре-ку'
    species_of_animals = ['Петух', 'Курица']


class Goat(Cow, Mammal):
    sound = 'Ме-е-е'
    species_of_animals = ['Козёл', 'Коза']


class Duck(Bird):
    sound = 'Кря-кря'
    species_of_animals = ['Селезень', 'Утка']


animals = {
    'grey':
        {'entity': Goose,
            'name': 'Серый',
            'weight': 8},
    'white':
        {'entity': Goose,
            'name': 'Белый',
            'weight': 7.5},
    'mary':
        {'entity':Cow,
        'name':'Манька',
        'weight':523},
    'barashek':
        {'entity':Sheep,
         'name':'Барашек',
         'weight':45},
    'kudrjavij':
        {'entity':Sheep,
         'name':'Кудрявый',
         'weight':42},
    'koko':
        {'entity':Chicken,
         'name':'Ко-Ко',
         'weight':2.1},
    'kukareku':
        {'entity':Chicken,
         'name':'Кукареку',
         'weight':1.7},
    'horns':
        {'entity':Goat,
         'name':'Рога',
         'weight':60},
    'hooves':
        {'entity':Goat,
         'name':'Копыта',
         'weight':63},
    'kryakva':
        {'entity': Duck,
         'name':'Кряква',
         'weight':2.4}
}
objs = dict()
for key, value in animals.items():
    objs.update({key: value['entity'](value['name'], value['weight'])})

rprint("Животное подаёт голос")
for key in objs.keys():
    animal = random.choice(list(animals.keys()))
    sex = random.choice(['male', 'female'])
    objs[key].set_sex(sex)
    objs[key].say()

rprint("Кормим животное")
for key in objs.keys():
    objs[key].feed_the_animal()

rprint("Гладим животное")
for key in objs.keys():
    objs[key].pet_the_animal()

rprint("Доим животное")
for key in objs.keys():
    if hasattr(objs[key], 'milking'):
        objs[key].milking()
    else:
        print(f'{objs[key].name}({objs[key].get_species_of_animals()}) не дойное животное.')

rprint("Собираем яйца")
for key in objs.keys():
    if hasattr(objs[key], 'collect_eggs'):
        objs[key].collect_eggs()
    else:
        print(f'{objs[key].name} ({objs[key].get_species_of_animals()}): не откладывает яйца.')

rprint("Стрижом")
for key in objs.keys():
    if hasattr(objs[key], 'shearing'):
        objs[key].shearing()
    else:
        print(f'{objs[key].name} ({objs[key].get_species_of_animals()}): не стрижотся.')

rprint("Выясняем самое тяжелое животное")
# print(max([key,weight from ]))
# print([value.name for value in objs.values() if value.weight == max(objs.values().weight)])

max_weight = 0
max_weight_name = None
m_weight = dict()
for value in objs.values():
    m_weight.update({value.name: value.weight})
    if value.weight > max_weight:
        max_weight = value.weight
        max_weight_name = value.name

# m_weight2 = {value.name: value.weight for value in objs.values()}
print(f'Самым тяжелым животным является {max_weight_name}. Вес: {max_weight} кг.')
print(f'Самым тяжелым животным является {max({value.name: value.weight for value in objs.values()}, key=m_weight.get)}.'
      f' Вес: {max(m_weight.values())} кг.')
print('Самым тяжелым животным является', max({value.name: value.weight for value in objs.values()}, key=m_weight.get))

rprint("Суммарный вес животных фермы")
print(f'Вес всех животных фермы: {sum([value.weight for value in objs.values()])} кг.')

