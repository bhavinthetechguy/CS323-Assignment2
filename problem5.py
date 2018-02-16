#Bhavinkumar Patel
#Jay Shah
#Nimit Doshi

import numpy as np
import math

L = np.zeros([2,2])
U = np.zeros([2,2])

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
    
    for k in range (1,11):
        epsilon = math.pow(10, (-2*k))
        A = np.matrix([[ epsilon , 1 ],[ 1, 1]])       
        b = np.matrix([[1+epsilon],[2]])
        Gaussian_Elimination(A)
        Elimination_Matrix(A)
        x =np.zeros(2)
        y =np.zeros(2)    
        Forward_Substitution(L,b,y)
        Back_Substitution(U,b,x)
        print "X:"
        for i in range(0,2):
            print np.float32(np.matrix(x[i]))
        print "\n"
        
if __name__ == "__main__":
    main()
