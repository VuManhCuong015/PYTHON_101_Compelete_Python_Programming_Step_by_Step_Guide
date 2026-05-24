"""
File Modes (Chế độ mở file)

Chế độ 'r' (Read - Chỉ đọc)
Chế độ 'w' (Write - Ghi mới hoàn toàn)
Chế độ 'a' (Append - Ghi nối đuôi)
Chế độ 'x' (Exclusive Creation - Tạo độc quyền)

Các Operations (Thao tác xử lý dữ liệu)
Thao tác Đọc (Dành cho chế độ 'r')
file.read(): Đọc hết toàn bộ file thành 1 chuỗi ký tự (String) duy nhất.
file.readline(): Đọc từng dòng một. Mỗi lần gọi hàm, nó sẽ đọc dòng tiếp theo.
file.readlines(): Đọc toàn bộ các dòng và nhét chúng vào một Danh sách (List), mỗi dòng là một phần tử.

Thao tác Ghi (Dành cho chế độ 'w', 'a')
file.write("chuỗi_chữ"): Ghi một chuỗi chữ vào file. Bạn phải tự thêm ký tự \n nếu muốn xuống dòng.
file.writelines(danh_sách): Ghi một danh sách các chuỗi chữ vào file cùng một lúc.
"""