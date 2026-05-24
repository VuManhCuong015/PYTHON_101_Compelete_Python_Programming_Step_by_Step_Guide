"""
installing external packages
Tải công cụ có sẵn về để
đỡ phải tự viết code từ đầu,
giúp làm việc nhanh và dễ dàng hơn.
"""
#ex1
#np (numpy viettat numerical python) tinh toan so hoc

# import numpy as np
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("Sum",np.sum(matrix))
# print("transpace:\n",np.transpose(matrix))

#np.TRANSPOSE la ma tran chuyen vi
#no se bien hang thanh cac cot va nguoc lai bien cot thanh hang

#ex2
# import numpy as np
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# matrix_cot = matrix.T          # Lật lần 1 (Hàng -> Cột)
# matrix_hang = matrix_cot.T     # Lật lần 2 (Cột -> Hàng)
# print("Kết quả quay về ban đầu:\n", matrix_hang)

#ex3
import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Lật lần 1: Từ Hàng chuyển thành Cột
matrix_cot = matrix.T
print("1. Kết quả dạng CÔT:\n", matrix_cot)

# Lật lần 2: Từ Cột quay ngược về Hàng
matrix_hang = matrix_cot.T
print("2. Kết quả quay về dạng HÀNG ban đầu:\n", matrix_hang)