#set ex 1
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)

my_set.add(7)
print(my_set)

#ex2
my_set = {1, 2, 3, 4, 5}

set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a | set_b
print(union_set)

intersection_set = set_a & set_b
print(intersection_set)

difference_set = set_a - set_b
print(difference_set)


#ex3
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print(unique_set)