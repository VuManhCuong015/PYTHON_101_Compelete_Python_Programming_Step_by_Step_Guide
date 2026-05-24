#ex1
def even_numbers(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = even_numbers(3)
for number in counter:
    print(number)

#ex2
def even_numbers():
    num = 0
    while True:
        yield num
        num += 2

even_gen = even_numbers()
for __ in range(5):
    print(next(even_gen))

#ex3
squares = (x * x for x in range(1, 6))

for square in squares:
    print(square)