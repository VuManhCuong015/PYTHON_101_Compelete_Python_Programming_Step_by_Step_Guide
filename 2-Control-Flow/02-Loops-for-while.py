#for dung khi ban muon bite lap lai code bao nhieu lan va muon duyet qua tung phan tu trong danh sach

#example for
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"toi thich an trai cay {fruit}")


#while neu ban chua biet xac dinh lap bao nhieu lan thi while no se lien tuc chay doan code cho den khi co dieu kien dung
#khi nao gap dieu kien sai no moi dung lai

#example while
correct_password = "manhcuong06"
enter_password = input("enter password")

#khi nhap sai bat nguoi dung nhap lai
while enter_password != correct_password:
    print("password doesn't match ")
    enter_password = input("re-enter password")

print("login successful ")
