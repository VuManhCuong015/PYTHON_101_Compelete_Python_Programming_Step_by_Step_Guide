#example 1
class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")


# Tạo đối tượng dog1 từ lớp Dog
dog1 = Dog(name="Buddy", breed="Golden Retriever")

# Gọi phương thức bark của đối tượng dog1
dog1.bark()

#example 2
class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")


# Tạo 3 đối tượng chó khác nhau
dog1 = Dog(name="Buddy", breed="Golden Retriever")
dog2 = Dog(name="Lucy", breed="Bulldog")
dog3 = Dog(name="Max", breed="Beagle")

# Ra lệnh cho từng chú chó sủa
dog1.bark()
dog2.bark()
dog3.bark()

#ex3
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


# Tạo một đối tượng hình tròn có bán kính bằng 5
circle1 = Circle(5)

# Tính và in ra diện tích của hình tròn này
print(circle1.area())