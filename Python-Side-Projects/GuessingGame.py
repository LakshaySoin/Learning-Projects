from random import randint

class Game:
    def __init__(self):
        self.__var = 'Hello! This is a guessing game'

    def Intro(self):
        global intro
        intro = self.__var
        return intro

    def Pick(self):
        self.__user = int(input("Pick a number from 1 - 10: "))
        global num1
        num1 = self.__user
        return num1

    def Random(self):
        self.__cpu = randint(0, 10)
        global num2
        num2 = self.__cpu
        return num2

    def Victory(self):
        if num1 == num2:
            return self.__user and self.cpu
            return "You won! :)"
        else:
            return "You lost :("

Object = Game()

print(Object.Intro())
print(Object.Pick())
print(Object.Random())
print(Object.Victory())