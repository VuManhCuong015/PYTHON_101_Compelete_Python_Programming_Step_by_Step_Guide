#break dung lai khong chay nua (thoat chuong trinh ngay laptuc)
#continue bor qua buoc do va tiep tuc buoc sau

#example break
# food = ["mon_1", "mon_2", "mon_3"]#khoi tao 1 list do an
#
# for do_an in food:
#     choice = input("xin hay chon 1 mon an")
#
#     if choice == "stop":
#         print("ban da ra lenh dung chuong trinh")#break de thoat
#         break
#
#     #neu khong nhap stop may se chay lenh print o duoi
#     print(f"ban vua nhap mon:{choice}.tiep tuc lap...\n")
#
# print("vong lap da ket thuc!")

#example1 continue
# for floor in range (1,6):
#     if floor == 3:#== phep so sanh ket qua tra ve true or false
#         print(f"tang {floor} dang sua chua!bo qua tang nay")
#         continue #khi go lenh nay may tinh bo qua lenh print o duoi de tiep tuc tang 4
#
#     print (f"shipper dang dao hang tai tang{floor}")
#
# print("shipper da giao hang xong ")

#example2 continue
numbers = [2,4,6,7,8,9]

for num in numbers:
    if num <= 5:
        continue
    if num % 2 != 0:#num % 2 phep chia lay so du != 0 phep so sanh khong bang hoac khac
        print(f"the first add numbers greater than 5 is {num}.")
        break