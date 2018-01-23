import csv
import numpy as np
f = open('matrix.csv', "rt", encoding='utf8')
data = list(csv.reader(f, skipinitialspace=True))
season = {"winter": -1, "summer": 1, "fall": 0, "spring": 0}
data = [[x.strip() for x in row] for row in data]
new_data = []
for row in data:
    new_data.append([int(row[0]), int(row[1]), season[row[2]]])
new_data = np.array(new_data)
m = max(new_data[:, 0])
n = max(new_data[:, 1])
A = np.zeros((m + 1, n + 1))
for row in new_data:
    A[row[0], row[1]] = row[2]


f = open('matrix.csv', "rt", encoding='utf8')
reader = csv.reader(f, skipinitialspace=True)

season = {"winter": -1, "summer": 1, "fall": 0, "spring": 0}
data = []
for row in reader:
    row = [x.strip() for x in row]
    row[2] = season[row[2]]
    row[1] = int(row[1])
    row[0] = int(row[0])
    data.append(row)

data = np.array(data)
print(data)
m = max(data[:, 0])
n = max(data[:, 1])
data_new = np.full((m + 1, n + 1), 999)
print(data_new)
for row in data:
    data_new[row[0], row[1]] = row[2]

    print(A[np.ix_([1, 2], [9, 10])])
