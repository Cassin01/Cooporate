#input.py
class Person:
    def __init__(self,age,name):
        self.__age = age
        self.__name = name
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name

    

p = Person(14, "Ayaya")
print(str(p.get_name()) + str(p.get_age()))
print(str(p.get_age()))