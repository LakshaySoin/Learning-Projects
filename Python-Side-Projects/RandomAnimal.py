import random

class Animals:
    def __init__(self):
        self.animals = ['dog', 'cat', 'lion', 'bird']

    def Randomly(self):
        self.picked = random.randint(0, len(self.animals) - 1)

    def Dog(self):
        if self.picked == 0:
            print("Woof!")
        else:
            pass

    def Cat(self):
        if self.picked == 1:
            print("Meow!")
        else:
            pass

    def Lion(self):
        if self.picked == 2:
            print("Roar!")
        else:
            pass
    def Bird(self):
        if self.picked == 3:
            print("Tweet!")
        else:
            pass

obj = Animals()
obj.Randomly()
obj.Dog()
obj.Cat()
obj.Bird()
obj.Lion()
