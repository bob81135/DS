def bin(m,n):
    tag = 1 
    for i in range(m,m-n,-1):
        tag*=i
    tag1 = 1
    for i in range(n,1,-1):
        tag1*=i
    return tag//tag1
print(bin(8,4))