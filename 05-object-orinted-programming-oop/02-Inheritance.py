#Inheritance (Tính kế thừa)
class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} the {self.breed} barks")


# Tạo đối tượng dog từ lớp Dog
dog = Dog(name="Buddy", breed="Golden Retriever")
# Gọi phương thức speak
dog.speak()