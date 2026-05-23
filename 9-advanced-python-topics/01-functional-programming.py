#example 1
#lambda la keyword py dung khai bao ham an danh anonymouse functions
# cho phep tao mot ham ngan gon tren mot dong duy naht va tu dong tra ve ket qua
# cua bieu thuc sau dau : ma khong can tu khoa return

add = lambda x, y: x + y

result = add(6, 9)
print(f"Result of lamda function: {result}")

#example 2
numbers = [1, 2, 3, 4, 5]
#map ap dung ham lambda len tung phan tu trong list numbers
#list dung de lam cac phep tinh va gom ket qua vao mot danh sach
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(f"Squared numbers: {squared_numbers}")


#ex3
numbers = [1, 2, 3, 4, 5, 6]
#filer duyet qua list number chi giu lai phan tu thoa man dieu kien chia het cho 2
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Even numbers: {even_numbers}")