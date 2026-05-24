#ex1
# def sum_list(lst):#tao mot ham sumlist
#     if not lst:#neu danh sach rong
#         return 0
#     else:#neu con phan tu ham se lay phan tu dau tien dem cong ket qua cua chinh ham do
#         #sau do truyen vao danhj sach tu vi tri so 1 tro di
#         return lst[0] + sum_list(lst[1:])
#
# numbers = [1, 2, 3, 4, 5]
# result = sum_list(numbers)#de quy xep chong cac tang
# print(f"The sum of the list is {result}")

#ex2
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(6)
print(f"The 6th Fibonacci number is {result}")