# import numpy as np
# x = np.arange(0,20)
# y1 = np.random.randint(4, 13, (20,))
# y2 = np.random.randint(18, 23, (20,))
# y3 = np.random.randint(25, 29, (20,))
# plt.scatter(x, y1, marker = "*", color="purple")
# plt.scatter(x, y2, marker = "h", color="pink")
# plt.scatter(x, y3, marker = "x", color="grey")
# plt.title("Scatter Plot")
# plt.show()
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y1 = [10, 18, 14, 22, 37, 22, 19, 22, 6]
y2 = [2, 17, 23, 13, 26, 19, 5, 39, 43]
y3 = [11, 13, 29, 30, 25, 4, 19, 44, 20]
plt.stackplot(x,y1,y2,y3, colors=["green", "red", "blue"])
plt.title("Stack Plot")
plt.show()