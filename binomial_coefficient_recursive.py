def bin(n,m):
    if(m==0 or n==m):
        return 1
    else:
        return bin(n-1,m)+bin(n-1,m-1)
print(bin(8,4))