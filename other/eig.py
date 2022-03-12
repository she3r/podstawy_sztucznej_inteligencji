from numpy.linalg import eig
import numpy as np

M = np.matrix([[1,0,0,0,0],[0,2,0,0,0],[0,0,3,0,0],[0,0,0,4,0],[0,0,0,0,5]])
print(M)

w,v = eig(M)
print(w**2,v, sep='\n')