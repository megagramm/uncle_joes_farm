import datetime

# Со всеми животными вам необходимо как-то взаимодействовать:
# feed all of them кормить
# milking cow and goats корову и коз доить
# shearing овец стричь
# collect eggs собирать яйца у кур, утки и гусей
# различать по голосам(коровы мычат, утки крякают и т.д.)

# name
# weight


# Задание 1:
# Нужно реализовать классы животных и определить методы взаимодействия с животными.
# ​Для каждого животного из списка должен существовать экземпляр класса.
# Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.​
#
# Задание 2:
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
#
# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.

# class Animal
# class Bird (Animal)
# class Mammal (Animal)


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
            return "Оно требует называть себя ОНИ"
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex

    def input_set_sex(self):
        sex = input('Укажите пол (m, male, f, female): ').lower()
        if sex not in ['m', 'male', 'f', 'female']:
            print('Ваши значения не подходят:')
            return
        if sex == 'm':
            sex = 'male'
        if sex == 'f':
            sex = 'female'
        self.set_sex(sex)

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
            print(self.sound)

    def pet_tha_animal(self):
        """Погладь животное"""
        self.say()


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


class Goose(Bird):
    sound = 'Га-га-га'
    __species_of_animals = ['Гусь', 'Гусыня']


class Cow(Mammal):
    sound = 'Муу-у'
    __species_of_animals = ['Бык', 'Корова']


class Sheep(Mammal):
    sound = 'Бе-е-е'
    __species_of_animals = ['Баран', 'Овца']


class Chicken(Bird):
    sound = 'Ку-ка-ре-ку'
    __species_of_animals = ['Петух', 'Курица']


class Goat(Mammal):
    sound = 'Ме-е-е'
    __species_of_animals = ['Козёл', 'Коза']


class Duck(Mammal):
    sound = 'Кря-кря'
    __species_of_animals = ['Селезень', 'Утка']

animals = {
    'grey':
        {'entity': 'Goose',
            'name': 'Серый',
            'weight': 8},
    'white':
        {'entity': 'Goose',
            'name': 'Белый',
            'weight': 7.5}
}

entitys = dict()
# entitys[animals.]

animals['grey']

# for key, value in animals.items():
#     key = value['entity'](value['name'], value['weight'])


# grey = Goose('Серый', 8)
# white = Goose('Белый', 7.5)
# grey.say()

mary = Cow('Манька', 523)

barashek = Sheep('Барашек', 45)
kudrjavij = Sheep('Кудрявый', 42)

koko = Chicken('Ко-Ко', 2.1)
kukareku = Chicken('Кукареку', 1.7)

horns = Goat('Рога', 60)
hooves = Goat('Копыта', 63)

kryakva = Duck('Кряква', 2.4)


print(horns.name, horns.get_sex())
horns.input_set_sex()
print(horns.name, horns.get_sex())

horns.pet_tha_animal()
