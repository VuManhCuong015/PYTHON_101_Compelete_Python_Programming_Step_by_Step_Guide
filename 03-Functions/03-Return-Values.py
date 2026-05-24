#ex1
# def greet():
#     return "Hello Python"#tra ve hello python
#
# message = greet()#gan greet vao message
# print(message)#print message

#ex2
# def multiply(x,y):
#     return x*y
#
# result = multiply(2,3)
# print(f"the result is {result}")

#ex3
def human_information(name,age,height,weight):
    return (name,age,height,weight)

name,age,height,weight = human_information("Vu",22,"185",85)
print(f"The name is {name}, the age is {age}, the height is {height}, the weight is {weight}")
