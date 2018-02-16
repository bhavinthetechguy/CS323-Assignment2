#Bhavinkumar Patel
#Jay Shah
#Nimit Doshi

import numpy as np
def Elimination_Matrix(A):

    L = np.zeros([9,9])
    U = np.zeros([9,9])
    for x in range(0,9):
        for y in range(0,9):
            A[x,y] =(A[x,y])
            U[x,y] = A[x,y]

    for n in range(0,9):
        for m in range(0,9):
            if (n==m):
                L[n,m] = 1
            if (n<m):
                division = (A[m,n]/A[n,n])
                L[m,n] = division
                for c in range(0,9):
                    A[m,c] = A[m,c] - (division*A[n,c])
                    U[m,c] = A[m,c]
    print "L:"
    print L
    print "U:"
    print U
    print "LU:"
    LU = np.dot(L,(U))
    print LU
    print "\n"
    b = np.matrix([[2],[5],[7],[1],[6],[9],[4],[8],[3]])
    x = np.zeros(9)
    Forward_Substitution(L,b,x)
    
    print "X in Forward Substitution"
    print "x:"
    for i in range(0,9):
        a=np.array (x[i])
        print a
    
    y =np.zeros(9)
    b1= np.matrix([[2],[5],[7],[1],[6],[9],[4],[8],[3]])
    Back_Substitution(U,b1,y)
    print "\n"
    print "X in Back Substitution"
    print "x:"
    for j in range(0,9):
        a1=np.float32((np.array(y[j])))
        print a1

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

def Back_Substitution(U,b1,y):
    m=U.shape[0]
    n=U.shape[1]
    if(m!=n):
        print 'Matrix is not square!'
        return
    for j in range(n-1,-1,-1):
        if U[j,j] == 0:
            print 'Matrix is singular!'
            return          # matrix is singular
        y[j] = b1[j]/U[j,j]
        for i in range(0,j):
            b1[i] = b1[i] - U[i,j]*y[j]

def main():
    A=np.matrix([[21,32,14,8,6,9,11,3,5],
                 [17,2,8,14,55,23,19,1,6],
                 [41,23,13,5,11,22,26,7,9],
                 [12,11,5,8,3,15,7,25,19],
                 [14,7,3,5,11,23,8,7,9],
                 [2,8,5,7,1,13,23,11,17],
                 [11,7,9,5,3,8,26,13,17],
                 [23,1,5,19,11,7,9,4,16],
                 [31,5,12,7,13,17,24,3,11]])

    Elimination_Matrix(A)
    
if __name__ == "__main__":    
    main()
