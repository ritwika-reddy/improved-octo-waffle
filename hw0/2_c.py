import numpy as np
np.random.seed(18898899)
N = 1000
X = np.random.normal(0, 1, N)


def Cost_fn(X, theta1, theta2, N):
    return (N / 2 * np.log(theta2) +
            N / 2 * np.log(2 * np.pi) + sum((X - theta1)**2) / 2 * theta2)


def delta_1(X, theta1, theta2, N):
    return -1 * (sum(X - theta1) / theta2)


def delta_2(X, theta1, theta2, N):
    return N / (2 * theta2) - sum((X - theta1)**2) / (2 * theta2 ** 2)


def my_gradient_descent(X, theta1, theta2, N, eta, iter):
    for i in range(1, iter):
        theta1 = theta1 + eta * delta_1(X, theta1, theta2, N)
        theta2 = theta2 + eta * delta_2(X, theta1, theta2, N)
        cost = Cost_fn(X, theta1, theta2, N)
        print(cost)
        if(cost < 0):
            break
    return theta1, theta2


theta1 = np.random.rand()
theta2 = np.random.rand()
eta = 0.00001
num_iter = 1000
theta1, theta2 = my_gradient_descent(X, theta1, theta2, N, eta, num_iter)
print(theta1, theta2)
