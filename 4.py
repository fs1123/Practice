# Write a Python program which solves Ax = b by using PA = LU. Test your result.
import scipy.linalg as linalg
import numpy as np

def lu_solve(A,b):
    # if A is not a np.ndarray, convert it to a np.ndarray for convenience.
    if type(A) != np.ndarray:
        A = np.array(A)
    if type(b) != np.ndarray:
        b = np.array(b)

    P, L, U = linalg.lu(A)
    m,n = A.shape

    # Forward elimination to solve L*y = Pb = c

    y = np.zeros(m)
    c = np.matmul(P.T,b)

    for i in range(m):
        y[i] = c[i] - np.inner(L[i,:i],y[:i])


    # Back substitution to solve U*x = y
    x = np.zeros(n)
    for j in range(n-1,-1,-1):
        x[j] = (y[j] - (np.inner(U[j,j+1:n],x[j+1:n])))/U[j,j]

    return x

if __name__ == '__main__':
    A = np.random.randn(3,3)
    b = np.random.randn(3)
    print(lu_solve(A,b))
    print(linalg.solve(A,b))