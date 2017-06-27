class Animals:
    max_weight = 600  # Максимальный вес животного в кг.
    weigth = None
    color = None

    def eat(self):
        print('eats feed')

    def speak(self):
        print('speaks')

    def sleep(self):
        print('sleeps')


class Cows(Animals):
    def speak(self):
        print('speaks: "Muuuu"')

    def eat(self):
        print('eats hay')

    def sleep(self):
        print('goes to cowshed')
        super().sleep()


class Goats(Animals):
    max_weight = 45

    def speak(self):
        print('Goat speaks: "Meeee"')

    def eat(self):
        print('eats grass')

    def sleep(self):
        print('goes to the fold')
        super().sleep()


class Sheeps(Animals):
    max_weight = 65

    def speak(self):
        print('Sheeps speaks: "Beeee"')

    def eat(self):
        print('eat grass')

    def sleep(self):
        print('goes to the sheepfold')
        super().sleep()


class Pigs(Animals):
    max_weight = 150

    def speak(self):
        print('Pig speaks: "Oink oink"')

    def eat(self):
        print('eats pig feet')


class Ducks(Animals):
    max_weight = 4

    def speak(self):
        print('Duck speaks: "Quarck-quarck"')

    def sleep(self):
        print('goes to coop')
        super().sleep()


class Chikens(Animals):
    max_weight = 4.5

    def speak(self):
        print('Chiken speaks: "cluck-cluck"')

    def sleep(self):
        print('goes to roots')
        super().sleep()


class Gooses(Animals):
    max_weight = 12

    def speak(self):
        print('Gooses speaks: "honk-honk"')

    def sleep(self):
        print('goes to coop')
        super().sleep()

