import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

#barh()
plt.barh(x, y)
plt.show()

#argument color
plt.bar(x, y, color = "red")
plt.show()

#colour name
plt.bar(x, y, color = "hotpink")
plt.show()

#hexa code colour
plt.bar(x, y, color = "#4CAF50")
plt.show()

#bar width
plt.bar(x, y, width = 0.1)
plt.show()

#Bar Height
plt.barh(x, y, height = 0.1)
plt.show()