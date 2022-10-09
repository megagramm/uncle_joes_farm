import datetime
import random

def rprint(string):
    """Формирует вывод текста на экран по правому краю"""
    print(f'\n{"="*20} {string:>80}\n')

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

    def __init__(self, name=None, weight=None):
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

    def pet_tha_animal(self):
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
            print(f'{self.name}: Можно собирать яйца только у самочки')
            return
        eggs = random.randint(0, 3)
        if eggs > 0:
            self.say()
            self.say()
            self.say()
            print(f'{self.name}({self.species_of_animals[1].lower()}) снесла {eggs} яйца. Вы их забрали, она очень недовольна')
        else:
            print(f'{self.name}({self.species_of_animals[1]}): Не удалось собрать ни одного яйца. '
                  f'Либо {self.species_of_animals[1].lower()} перестала нестись, либо она их прячет')

    def shearing(self):
        """Стричь"""
        print('Нельзя стричь птиц')

class Mammal(Animal):
    """Подкласс живых существ"""
    mammal_attr = {
        'nose': True,
        'mouth': True,
        'teeth': True
    }

    def __init__(self, name, weight):
        self.attributes.update(self.mammal_attr)
        self.name = name
        self.weight = weight

    def collect_eggs(self):
        """Собирать яйца"""
        if self.get_sex() in ['male', 'female']:
            species_of_animals = self.species_of_animals[0] if self.get_sex() == 'male' else self.species_of_animals[1]
            print(f'{self.name}({species_of_animals.lower()}) Нельзя собирать яйца у млекопитающих')
        else:
            print(f'{self.name} Нельзя собирать яйца у млекопитающих')

    def shearing(self):
        """Стричь"""
        """Определить, стригут ли этих животных. Подстричь, уменьшить вес."""
        ...


class Goose(Bird):
    sound = 'Га-га-га'
    species_of_animals = ['Гусь', 'Гусыня']


class Cow(Mammal):
    sound = 'Муу-у'
    species_of_animals = ['Бык', 'Корова']

    def milking(self):
        """Доить"""
        if self.get_sex()=='female':
            print(f'{self.name} ({self.get_species_of_animals()}): {self.get_species_of_animals()} подоена')
            return
        print(f'{self.name} нельзя подоить')


class Sheep(Mammal):
    sound = 'Бе-е-е'
    species_of_animals = ['Баран', 'Овца']


class Chicken(Bird):
    sound = 'Ку-ка-ре-ку'
    species_of_animals = ['Петух', 'Курица']


class Goat(Mammal):
    sound = 'Ме-е-е'
    species_of_animals = ['Козёл', 'Коза']


class Duck(Bird):
    sound = 'Кря-кря'
    species_of_animals = ['Селезень', 'Утка']


animals = {
    'grey':
        {'entity': 'Goose',
            'name': 'Серый',
            'weight': 8},
    'white':
        {'entity': 'Goose',
            'name': 'Белый',
            'weight': 7.5},
    'mary':
        {'entity':'Cow',
        'name':'Манька',
        'weight':523},
    'barashek':
        {'entity':'Sheep',
         'name':'Барашек',
         'weight':45},
'kudrjavij':
        {'entity':'Sheep',
         'name':'Кудрявый',
         'weight':42},
'koko':
        {'entity':'Chicken',
         'name':'Ко-Ко',
         'weight':2.1},
'kukareku':
        {'entity':'Chicken',
         'name':'Кукареку',
         'weight':1.7},
'horns':
        {'entity':'Goat',
         'name':'Рога',
         'weight':60},
'hooves':
        {'entity':'Goat',
         'name':'Копыта',
         'weight':63},
'kryakva':
        {'entity': 'Duck',
         'name':'Кряква',
         'weight':2.4}
}

for key, value in animals.items():
    print(f'{key} = {value["entity"]}("{value["name"]}", {value["weight"]})')
    exec("{} = {}('{}',{})".format(key, value["entity"], value["name"], value["weight"]))

# print("""
# Ферма запонена животными
#
# вы можете делать разные действия с животными.
# Введите команду:
#  say/говорить
#  feed/кормить
#  pet/гладить
#  collect/собрать яйца
#  shearing/стричь
#  milking/доить
#
# """)
rprint("Животное подаёт голос")
for i in range(4):
    animal = random.choice(list(animals.keys()))
    sex = random.choice(['male', 'female'])
    exec("{}.set_sex('{}')".format(animal, sex))
    exec("{}.say()".format(animal))

rprint("Кормим животное")
for i in range(4):
    exec("{}.feed_the_animal()".format(random.choice(list(animals.keys()))))

rprint("Гладим животное")
for i in range(4):
    exec("{}.pet_tha_animal()".format(random.choice(list(animals.keys()))))

rprint("Доим животное")

x = Cow('xxx', 8)
# try:
# x.milking()
if hasattr(x,'milking'):
    print('есть вымя!')
else:
    print('нет вымени!')

# except (AttributeError):
#     print(x.name,'нельзя доить')

for i in range(4):
    animal = random.choice(list(animals.keys()))
    print(animal)
    sex = random.choice(['male', 'female'])
    print(sex)
    exec("{}.set_sex('{}')".format(animal, sex))
    print(animals[animal]['entity'])
    if hasattr(exec("{}".format(animal)), 'milking'):
        print('есть вымя')
    else:
        print('нет вымени')
        #  and callable(getattr(Dynamo, key))
    # exec("{}.milking()".format(animal))
"""

rprint("Собираем яйца")
for i in range(4):
    animal = random.choice(list(animals.keys()))
    exec("{}.set_sex(None)".format(animal))
    exec("{}.collect_eggs()".format(animal))
    exec("{}.set_sex('male')".format(animal))
    exec("{}.collect_eggs()".format(animal))
    exec("{}.set_sex('female')".format(animal))
    exec("{}.collect_eggs()".format(animal))
    print()
"""

