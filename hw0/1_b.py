import matplotlib.pyplot as plt
import numpy as np

np.random.seed(18898899)

N = 100
x1 = np.random.normal(0, 1, N)
x2 = np.random.normal(0, 1, N)

plt.scatter(x1, x2)
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Scatter plot of (X1,X2)')
plt.savefig('1_b.png')
plt.show()
