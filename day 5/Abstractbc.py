# ABC (Abstract Base Class)
from abc import ABC, abstractmethod

# Create an abstract class
class Animal(ABC):
   
    @abstractmethod
    def make_sound(self):
        pass
   
    @abstractmethod
    def move(self):
        print("Hello")
        return "Namaste"
   
    def sleep(self):
        print("Zzz... sleeping")
        return