#Polymorphism (Tính đa hình)
#ex1
# class Animal:
#
#     def speak(self):
#         print("Animal speaks")
#
#
# class Dog(Animal):
#
#     def speak(self):
#         print("Dog Barks")
#
#
# class Cat(Animal):
#
#     def speak(self):
#         print("Cat Meows")
#
# # Tạo danh sách chứa các đối tượng Dog và Cat
# animals = [Dog(), Cat()]
#
# # Vòng lặp duyệt qua từng đối tượng và gọi phương thức speak()
# for animal in animals:
#     animal.speak()

#ex2
class Bird:

    def speak(self):
        print("Bird Chirps")

class Dog:

    def speak(self):
        print("Dog Barks")


def animal_speck(animal):#ra lenh cho animal tuc hien hanh dong
    animal.speak()

#khoi tao doi tuong
bird = Bird()
dog = Dog()

#goi ham thuc thi kich hoat hanh dong 
animal_speck(bird)
animal_speck(dog)