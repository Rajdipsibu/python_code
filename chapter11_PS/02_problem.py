class Animel:
    pass
class Pets(Animel):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
        print('bow bow !!')

d=Dog()
d.bark()