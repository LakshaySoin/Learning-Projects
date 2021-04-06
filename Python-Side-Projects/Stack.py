class Stack:
    def __init__(self):
        self.__empty = []

    def push(self, val):
        self.__empty.append(val)

    def pop(self):
        num = self.__empty[-1]
        del self.__empty[-1]
        return num

Stackobject = Stack()

Stackobject.push(3)
Stackobject.push(2)
Stackobject.push(1)

print(Stackobject.pop())
print(Stackobject.pop())
print(Stackobject.pop())
