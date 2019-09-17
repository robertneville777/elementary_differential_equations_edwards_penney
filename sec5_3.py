import numpy as np
import sec5_3_funcs as sec5_3_funcs
import sympy as sym
from sympy.matrices import Matrix
from sympy import Symbol
# from sympy import *
# from sympy import init_session
# init_session()

# Problem 1
A = np.array([[2,-3],[4,7]])
B = np.array([[3,-4],[5,1]])

ans_1a = 2*A + 3*B
print(ans_1a)
print("\n")

ans_1b = 3*A - 2*B
print(ans_1b)
print("\n")

ans_1c = A@B # Matrix Multiply
print(ans_1c)
print("\n")

ans_1d = B@A
print(ans_1d)
print("\n")

# Problem 3 is more of the same. Did problem 5 by hand (do this symbolically?)

A1 = np.array([[2,1],[-3,2]])
A2 = np.array([[1,3],[-1,-2]])
B  = np.array([[2,4],[1,2]])

ans_7a = np.linalg.det(A1@B)
ans_7b = np.linalg.det(A2@B)
ans_7c1 = np.linalg.det(A1)
ans_7c2 = np.linalg.det(B)
ans_7c3 = ans_7c1*ans_7c2
print(ans_7a)
print(ans_7c1)
print(ans_7c2)
print(ans_7c3)
print("\n")

# Problems 21 - 29
t = Symbol('t')

print("Problem 21:")
P  = Matrix([[4,2],[-3,-1]])
x1 = sym.exp(t)*Matrix([2,-3])
x2 = sym.exp(2*t)*Matrix([1,-1])
sec5_3_funcs.verify_wronskian_dispsolution(P,x1,x2)

print("Problem 23:")
P  = Matrix([[4,2],[-3,-1]])
x1 = sym.exp(t)*Matrix([2,-3])
x2 = sym.exp(2*t)*Matrix([1,-1])
sec5_3_funcs.verify_wronskian_dispsolution(P,x1,x2)

print("Problem 25:")
P  = Matrix([[4,-3],[6,-7]])
x1 = sym.exp(2*t)*Matrix([3,2])
x2 = sym.exp(-5*t)*Matrix([1,3])
sec5_3_funcs.verify_wronskian_dispsolution(P,x1,x2)

print("Problem 27:")
P  = Matrix([[0,1,1],[1,0,1],[1,1,0]])
x1 = sym.exp(2*t)*Matrix([1,1,1])
x2 = sym.exp(-t)*Matrix([1,0,-1])
sec5_3_funcs.verify_wronskian_dispsolution(P,x1,x2)