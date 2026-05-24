#example 1
# def kiem_tra_tuoi(tuoi):
#     if tuoi < 0:
#         raise ValueError("Lỗi rồi: Tuổi của một người không thể là số âm!")
#     else:
#         print(f"Tuổi hợp lệ: {tuoi} tuổi. Đang tiến hành đăng ký tài khoản...")
#
#
# # Thử nghiệm chạy hàm
# try:
#     nhap_tuoi = int(input("nhap so tuoi: "))
#     kiem_tra_tuoi(nhap_tuoi)
#
# except ValueError as e:
#     print(f"Hệ thống bảo mật chặn lại: {e}")


#example 2
# def check_positive_number(number):
#     if number < 0:
#         raise ValueError("The number must be positive")
#     print(f"The number {number} is valid")
#
# check_positive_number(5)

#example 3
def validate_user(age, username):
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    if age < 18:
        raise ValueError("user must be at least 18 years old")
    if len(username) < 3:
        raise ValueError("username must be at least 3 characters long")

    print("user validated successfully")

try:
    username = input("Enter your username: ")
    age = int(input("Enter your age: "))

    validate_user(age, username)

except ValueError as e:
    print(f"He thong phat hien loi gia tri: {e}")

except TypeError as e:
    print(f"he thong phat hien loi kieu du lieu: {e}")
    