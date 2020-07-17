import sys
sys.setrecursionlimit(100000000)
def ackerman(m,n):
    while(m!=0):
        if(n==0):
            n = 1
        else:
            n = ackerman(m,n-1)
        m -=1
    return n+1
print(ackerman(3,2))