class Animal:
    species = 'unknown'
    scream = 'unknown'

    # конструктор
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def nourish(self):
        print('Покормить', self.species, self.name, '-', self.weight, 'кг')

    def screaming(self):
        print('Они', self.scream)


class Poultry(Animal):  # Домашня птица
    def act(self):
        print('Собрать яйца у', self.name)


class Chicken(Poultry):
    Animal.species = 'курицу'
    Animal.scream = 'кудахчaт'


chicken1 = Chicken('Ко-Ко', 3)
chicken1.nourish()

chicken2 = Chicken('Кукареку', 3)
chicken2.nourish()
chicken2.screaming()


class Goose(Poultry):
    Animal.species = 'гуся'
    Animal.scream = 'шепят'


goose1 = Goose('Серый', 4)
goose1.nourish()

goose2 = Goose('Белый', 5)
goose2.nourish()
goose2.screaming()


class Duck(Poultry):
    Animal.species = 'утку'
    Animal.scream = 'крякают'


duck1 = Duck('Кряква', 3)
duck1.nourish()
duck1.screaming()


class GiveWoolenAnimals(Animal):  # Животные, дающие шерсть
    def act(self):
        print('Подстричь', self.name)


class Sheep(GiveWoolenAnimals):
    Animal.species = 'овцу'
    Animal.scream = 'блеют'


sheep1 = Sheep('Барашек', 80)
sheep1.nourish()

sheep2 = Sheep('Кудрявый', 78)
sheep2.nourish()
sheep2.screaming()


class GiveMilkAnimals(Animal):  # Животные, дающие молоко
    def act(self):
        print('Подоить', self.name)


class Cow(GiveMilkAnimals):
    Animal.species = 'корову'
    Animal.scream = 'мычат'


cow1 = Cow('Манька', 210)
cow1.nourish()
cow1.screaming()


class Goat(GiveMilkAnimals):
    Animal.species = 'козу'
    Animal.scream = 'блеют'


goat1 = Goat('Рога', 92)
goat1.nourish()

goat2 = Goat('Копыта', 85)
goat2.nourish()
goat2.screaming()

all_animals = [chicken1, chicken2, goose1, goose2, duck1, sheep1, sheep2, cow1, goat1, goat2]
for animal in all_animals:
    animal.act()
weights = [animal.weight for animal in all_animals]
print('Максимальный вес животного -', max(weights), 'кг.')
