class Runner:
    def __init__(self):
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
        self.__value = p.get_name()
        print(str(p.get_name()) + str(p.get_age()))
        print(str(p.get_age()))
    def get_value(self):
        return self.__value
