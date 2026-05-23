"""
decorator la
công cụ giúp mở rộng/thay đổi hành vi của một hàm
mà không cần sửa trực tiếp code bên trong hàm đó.

Sử dụng ký tự @ đặt ngay phía trên hàm cần bổ sung tính năng.

Cách hoạt động: Nhận hàm gốc làm tham số $\rightarrow$ Bọc hàm gốc bằng một hàm mới (wrapper)
chứa logic bổ sung $\rightarrow$ Trả về hàm mới đó.

Sử dụng cú pháp *args và kwargs
ở hàm bọc để truyền dữ liệu linh hoạt cho hàm gốc.
"""
#ex1
def my_decorator(func):
    #ham boc them cac hanh dong bo sung truoc va sau khi ham goc chay
    def wrapper():
        print("something is happening before the function is called.")
        func()
        print("something is happening after the function is called.")
    return wrapper#tra ve ham boc da dc them tinh nang


#du dung decorator vo ham say hello
@my_decorator
def say_hello():
    print("Hello!")

#goi ham
say_hello()

#ex2
def greet_decorator(name):
    def decorator(func):
        def wrapper():
            print(f"Hello, {name}")
            func()
        return wrapper
    return decorator

@greet_decorator("Sophia")
def say_hello():
    print("Welcome to the tutorial!")

say_hello()