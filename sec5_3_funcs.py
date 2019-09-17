# Code Author: robertneville777
# Code Date Creation: 9-14-2019
# Code Date Revision: 9-14-2019

# Text: Elementary Differential Equations
# Author: Edwards and Penney
# Edition: 5th
# Section: 5.3
# Problems: 21-30

# Description: First verify that given vectors are solutions to
#              given system. Then use Wronskian to show that
#              they are linearly independent. Finally, display
#              the general solution of the system.

import sympy as sym
from sympy.matrices import Matrix
from sympy import Symbol

def verify_wronskian_dispsolution(P, x1, x2):

    t = Symbol('t')

    x1_prime = x1.diff(t)
    x2_prime = x2.diff(t)

    if x1_prime == P*x1:
        print("x1 is a solution to the system")
    else:
        print("x1 is not a solution to the system")

    if x2_prime == P*x2:
        print("x2 is a solution to the system")
    else:
        print("x2 is not a solution to the system")

    # Create matrix from x1 and x2
    W = Matrix([x1.T,x2.T])
    W = W.T
    W = W.det()

    print('Wronskian of x1 and x2:')
    print(W)

    # Print general solution of system
    c1 = Symbol('c1')
    c2 = Symbol('c2')

    x = c1*x1 + c2*x2
    sym.pprint(x)
    print('\n')