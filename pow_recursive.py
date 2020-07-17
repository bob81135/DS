def pow(n,m):
    if(m==0):
        return 1
    else:
        return pow(n,m-1)*n
print(pow(2,10))