import numpy as np

np.random.seed(100089)

# Empirically compute the probability that a point (X1,X2)
# falls within a circle of radius 0.5 centered at (0,0)

N = 100
x1 = np.random.normal(0, 1, N)
x2 = np.random.normal(0, 1, N)
points = np.column_stack((x1, x2))

# The matrix points stores all of the data points.
# We find the norm of each data and see if the norm
# is less than the radius of the circle.

print(sum(0.5 - (np.sqrt(np.sum(points**2, axis=-1))) > 0))

np.random.seed(19)
N = 100
x1 = np.random.normal(0, 1, N)
x2 = np.random.normal(0, 1, N)
x3 = np.random.normal(0, 1, N)
points = np.column_stack((x1, x2, x3))

# The matrix points stores all of the data points.
# We find the norm of each data and see if the norm
# is less than the radius of the circle.

print(sum((0.5 - (np.sqrt(np.sum(points**2, axis=-1)))) > 0))

np.random.seed(1800000)
N = 1000
x1 = np.random.normal(0, 1, N)
x2 = np.random.normal(0, 1, N)
x3 = np.random.normal(0, 1, N)
points = np.column_stack((x1, x2, x3))
points = np.column_stack((points, x3))
print(points)
# The matrix points stores all of the data points.
# We find the norm of each data and see if the norm
# is less than the radius of the circle.

print(sum(0.5 - (np.sqrt(np.sum(points**2, axis=-1))) > 0))

N = 100
points = np.random.normal(0, 1, N)
for x in range(2, 1000):
    x = np.random.normal(0, 1, N)
    points = np.column_stack((x, points))

print(sum(0.5 - (np.sqrt(np.sum(points**2, axis=-1))) > 0))
