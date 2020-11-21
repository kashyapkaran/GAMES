#https://youtu.be/JeznW_7DlB0?t=749
#oop (object oriented Programming)

class Dog:

    def __init__(self, name):
        self.name = name
        print(name)


    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

d = Dog("Karan")