import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
#khoi tao he truc toa do Oxy
x = [1, 2, 3, 4, 5]#tao truc ngang(truc hoanh) x
y = [10, 20, 30, 40, 25]#tao truc doc(truc tung) y

plt.plot(x, y, marker='o')
plt.title("Simple line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()#hien thi ket qua