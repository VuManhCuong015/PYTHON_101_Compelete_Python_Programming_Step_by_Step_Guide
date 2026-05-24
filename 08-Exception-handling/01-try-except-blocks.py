#try - except: Dùng để hứng và xử lý
# khi có tai nạn xảy ra,
# giữ cho phần mềm luôn chạy ổn định.

#example 1
# try:
#     value = int(input("Enter a number: "))
#     print("100 devided by your number is: ", 100 / value)
#
# except ZeroDivisionError:
#     print("error: cannot divide by zero")
#
# except ValueError:
#     print("Error: Please enter a valid number")

#example 2
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:#chay khi ko tim thay file
    print("error: the file does not exist")
else:#chi chay khi try hoat dong muot ma khong gap bat ki loi gi 
    print("file read successfully")
finally:
    print("Execution complete")