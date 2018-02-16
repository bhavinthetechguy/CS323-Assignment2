#Bhavinkumar Patel
#Jay Shah
#Nimit Doshi

import numpy as np
import math

L = np.zeros([4,4])
U = np.zeros([4,4])

def Gaussian_Elimination(A):
    m=A.shape[0]
    n=A.shape[1]
    if(m!=n):
        print 'Matrix is not square!'
        return
    for k in range(0,n-1):
        if A[k,k] == 0:
            return
        for i in range(k+1,n):
            A[i,k]=np.float32(A[i,k]/A[k,k])
        for j in range(k+1,n):
            for i in range(k+1,n):
                A[i,j]-=np.float32(A[i,k]*A[k,j])
                A[i,j] = np.float32(A[i,j])
                
def Elimination_Matrix(A): 
    np.fill_diagonal(L,1) 
    x = A.shape[0]
    for q in range(0,x):
        for w in range(0,q):
            L[q,w] = A[q,w]
    c = 0
    x=A.shape[0]
    for r in range(0,x):      
        for t in range(c,x):
            U[r,t] = A[r,t]
        c = c+1

def Forward_Substitution(L,b,x):
    m=L.shape[0]
    n=L.shape[1]
    if(m!=n):
        print 'Matrix is not square!'
        return
    for j in range(0,n):
        if L[j,j] == 0:
            print 'Matrix is singular!'
            return          # matrix is singular
        x[j] = b[j]/L[j,j]
        for i in range(j+1,n):
            b[i] = b[i] - L[i,j]*x[j]

def Back_Substitution(U,b,x):
    m=U.shape[0]
    n=U.shape[1]
    if(m!=n):
        print 'Matrix is not square!'
        return
    for j in range(n-1,-1,-1):
        if U[j,j] == 0:
            print 'Matrix is singular!'
            return          # matrix is singular
        x[j] = b[j]/U[j,j]
        for i in range(0,j):
            b[i] = b[i] - U[i,j]*x[j]

def main():
    A=np.matrix([[21.0,67.0,88.0,73.0],
                 [76.0,63.0,7.0,20.0],
                 [0.0,85.0,56.0,54.0],
                 [19.3,43.0,30.2,29.4]],dtype='f')
    
    b=np.matrix([[141.0], [109.0], [218.0], [93.7]])
    Gaussian_Elimination(A)
    Elimination_Matrix(A)
    x = np.zeros([4,1])
    
    y = np.zeros(4)
    Forward_Substitution(L,b,y)
    Back_Substitution(U,b,x)
   
    print ' '
    print "Values of X:"
    print x
    A1=np.matrix([[21.0,67.0,88.0,73.0],
                 [76.0,63.0,7.0,20.0],
                 [0.0,85.0,56.0,54.0],
                 [19.3,43.0,30.2,29.4]],dtype='f')
    b1=np.matrix([[141.0], [109.0], [218.0], [93.7]])

    print "\n"
    print "AX:"
    Ax = np.dot(A1,x)
    print Ax
    print "\n"

    print "r:"
    r = np.subtract((b1) ,(Ax))
    print np.float64(r)
    x1 = np.zeros([4,1])
    y1 = np.zeros(4)
    Forward_Substitution(L,r,y1)
    Back_Substitution(U,r,x1)
    print ' '
    print "Values of Z:"
    print x1
    print "\n"
    print "Values of X + Z:"
    xz = np.add( x , x1)
    print xz
    print "\n"
    print "New value of B:"
    new = np.dot(A1, xz)
    print new
        
if __name__ == "__main__":
    main()
