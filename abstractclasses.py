from abc import ABC,abstractmethod

class Pets(ABC):

    @abstractmethod
    def MakeSound(sound):
        print(sound)


class Dog(Pets):
    def MakeSound(sound):
        print("Bark Bark")
class Cat(Pets):
    def MakeSound(sound):
        print("Meow Meow")
class Snake(Pets):

    def MakeSound(sound):

        print("Hissssss")


dog = Dog()
cat = Cat()
snake = Snake()

dog.MakeSound()
cat.MakeSound()
snake.MakeSound()

