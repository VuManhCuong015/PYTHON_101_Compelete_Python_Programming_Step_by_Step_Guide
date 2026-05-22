"""
Module: Là một file code Python đơn lẻ (có đuôi .py). Bạn gom các hàm,
các biến có liên quan vào file này để dùng đi dùng lại cho gọn.

Package: Là một thư mục (folder) chứa nhiều file Module gom lại với nhau.
Giống như một cái hộp to chứa các hộp nhỏ bên trong để quản lý cho dễ.
"""
#ex1
# import my_module
#
# print(my_module.greet("cuong"))
# print(my_module.add(7,8))

#ex2
# from my_module import greet
# print(greet("learning python"))

#ex3
from my_package.math import multiply
from my_package.strings_ops import to_uppercase

print(multiply(6 , 7))
print(to_uppercase("python"))