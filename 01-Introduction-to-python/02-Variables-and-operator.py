"""
Trong Python, Variable (Biến) và Operator (Toán tử) là hai khái niệm cốt lõi luôn đi đôi với nhau:
Biến dùng để lưu trữ dữ liệu,
còn Toán tử dùng để tính toán và xử lý các dữ liệu đó.
"""
#example:variable
# age = 20#tao mot bien ten age va gan gia tri la 20
# name = "manh cuong"
#
# print(age, name)

#example:operator
"""
    operator:toan tu + - * /
"""

a = float(input("enter number a"))
b = float(input("enter number b"))

#addition
addition_result = a + b
print(addition_result)

#subtraction
subtraction_result = a - b
print(subtraction_result)

#Multiplication
multiplication_result = a * b
print(multiplication_result)

#division
division_result = a / b
print(division_result)

#floor division
floor_division = a // b
print(floor_division)

#Modulus
remainder = a % b
print(remainder)

#Exponentiation operator so mu 2^2 = 2 * 2 = 4
power = a ** b
print("a ** b =", power)


