import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 10)
y = x ** 2

fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # Left, bottom, width, height
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes2.legend()

axes1.plot(x, y, 'r', label="curve1")
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')

axes2.plot(y, x, 'g', label="curve2")
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('insert title')

plt.show()
