#ex1
# my_list = [1, "apple", 3.14, True]
#
# first_item = my_list[0]
# last_item = my_list[-1]
#
# print(f"First item: {first_item}, Last item: {last_item}")

#ex2
# my_list = [1, "apple", 3.14, True]
#
# my_list[1] = "orange"
# print(my_list)
#
# my_list.append("grape")
# print(my_list)
#
# my_list.remove(3.14)
# print(my_list)

#ex3
my_list = [1, "apple", 3.14, True]
sub_list = my_list[1:3]
print(sub_list)

#ex4
my_list = [1, "apple", 3.14, True]

list_length = len(my_list)
print(f"Length of list: {list_length}")

my_list.sort()
print(my_list)

numbers = [3.14, 1, 5, 2]
numbers.sort()
print(numbers)  # Kết quả: [1, 2, 3.14, 5]

