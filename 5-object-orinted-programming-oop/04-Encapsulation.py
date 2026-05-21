#Encapsulation (Tính đóng gói)
"""
Bảo mật và Kiểm soát dữ liệu:
Ngăn chặn việc dữ liệu bị thay đổi một cách vô ý hoặc cố ý làm sai lệch logic chương trình
(ví dụ: không cho phép sửa số dư tài khoản thành số âm, không cho phép sửa tuổi của một người thành số âm).

Dễ thay đổi code bên trong:
Sau này nếu ngân hàng muốn thay đổi công thức tính số dư
(ví dụ: trừ thêm phí duy trì), họ chỉ cần sửa đúng cái hàm deposit hoặc withdraw bên trong Class.
Những người dùng code ở bên ngoài hoàn toàn không bị ảnh hưởng gì cả, họ vẫn gọi hàm như cũ.
"""
#example 1:
# class BankAccount:
#
#     def __init__(self, owner, balance):
#         self.owner = owner
#         # thuoc tinh co dau 2 __ phia truoc -> bien Private (da duoc dong goi va an di)
#         self.__balance = balance
#
#     #ham cong khai (Public) de xem so du tai khoan (Getter)
#     def get_balance(self):
#         return self.__balance
#
#     #ham cong khai (Public) de nap tien (Setter) - co kiem tra dieu kien
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Nạp thành công {amount}!")
#         else:
#             print("Số tiền nạp không hợp lệ!")
#
# # chay thu code
# account = BankAccount("Nguyễn Văn A", 1000)
#
# # co tinh truy cap truc tiep se bi loi
# # print(account.__balance)  #may se bao loi: AttributeError (vi bien nay da bi an)
#
# # truy cap hop e qua hamm cong khai
# print(f"Số dư hiện tại: {account.get_balance()}")  # In ra: 1000
#
# # nap tien dung quy trinh
# account.deposit(500)  # In ra:nap thanh cong
# print(f"Số dư mới: {account.get_balance()}")  # In ra: 1500

#example 2:
# class Account:
#
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("deposit must be positive.")
#
#     def get_balance(self):#__balace khong the doc truc tiep tu ngoai         #
#         #nen ham get_balance tao ra voi nhiem vu duy nhat la doc so du hien tai tu ben trong
#         #roi return ra cho nguoi dung xem *nhung ham nhu nay duoc goi la getter
#         return self.__balance
#
#
# # tao doi tuong account  voi so du ban dau la 1000
# account = Account(1000)
#
# # nap them 500 vao tai khoan
# account.deposit(500)
#
# # lay ra va in so du hien tai dang co trong tai khoan
# print(account.get_balance())

# example 2 slightly different
class Account:

    def __init__(self, balance):
        self.__balance = balance

    def set_balance(self, balance):
        if balance >= 0:#kiem tra xem so moi truyen vao > hoac = 0 khong
            self.__balance = balance#dong nay chay khi dkien if dung
            #dau - phep gan thay the so moi balnce ghi de con so cu dang nam trong slf__balance
        else:
            print("Balance cannot be negative.")

    def get_balance(self):
        return self.__balance


account = Account(1000)
account.set_balance(1200)#so du cu 1000 bij xoa bo hoan toan thay the bang 1200
# nhung ham co nhiem vu cai dat hay thay doi truc tiep gia tri cua bien an nhu nay goi la mot setter
print(account.get_balance())




