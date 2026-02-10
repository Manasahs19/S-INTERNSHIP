from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def sleep(self):
        print("it's Sleeping")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")       

class Cow(Animal):
    def sound(self):
        print("Moo")

d=Dog()
d.sound()
c=Cat()
c.sound()
co=Cow()
co.sound()
d.sleep()         