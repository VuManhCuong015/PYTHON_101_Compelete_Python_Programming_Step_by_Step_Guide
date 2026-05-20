#ex1
my_tuple = ('apple', 'banana', 'cherry')

print(my_tuple[0])
print(my_tuple[1])

#ex2
tuple1 = (1, 2, 3)
tuple2 = (4, 5)

new_tuple = tuple1 + tuple2
print(new_tuple)

repeated_tuple = tuple1 * 2
print(repeated_tuple)

#ex3
nested_tuple = ((1, 2), (3, 4), (5, 6))
# vitri           0       1        2
print(nested_tuple[1][0])# nested 1 boc tach tra ve tuple con la 3 va 4
# (3,4) tuong duong 0 va 1 khi in ra se lla 3 vi chi muc thu 2 la 0


#ex4
my_tuple = (1, 2, 3, 2)
print(my_tuple.count(2))
print(my_tuple.index(3))