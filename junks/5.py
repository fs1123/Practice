import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

A1 = np.array([[0, 0], [0, 0.27]])
A2 = np.array([[-.139, .263], [.246, .224]])
A3 = np.array([[.17, -.215], [.222, .176]])
A4 = np.array([[.781, .034], [-.032, .739]])
A = [A1, A2, A3, A4]

d1 = np.array([.5, 0])
d2 = np.array([.57, -.036])
d3 = np.array([.408, .0893])
d4 = np.array([.1075, .27])
d = [d1, d2, d3, d4]

p = (.02, .15, .13, .70)

z0 = np.random.randn(2)
z_list = [z0]
for i in range(1000):
    num = np.random.choice(4, 1, p=p)[0]
    z_list.append(np.dot(A[num], z_list[i]) + d[num])

x = [z[0] for z in z_list]
y = [z[1] for z in z_list]

plt.scatter(x, y)