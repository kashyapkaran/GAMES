import numpy as np

row_vector = np.array([10, 15, 20])
# print(row_vector)

column_vector = np.array([10, 20, 30])
# print(column_vector)

matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(np.dot(row_vector, column_vector))
