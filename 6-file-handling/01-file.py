# Chế độ 'w' sẽ tự động tạo file example.txt nếu chưa có.
# Nếu file đã có sẵn, nó sẽ XOÁ SẠCH nội dung cũ để ghi nội dung mới.
file = open('example.txt', 'w')
file.write('Xin chao, day la noi dung moi!')
file.close()

# Chế độ 'a' cũng tự động tạo file nếu chưa có.
# Nhưng nếu file đã có sẵn, nó sẽ ghi chèn thêm vào cuối file (không xoá bài cũ).
file = open('example.txt', 'a')
file.write('\nDay la dong chu duoc viet them.')
file.close()