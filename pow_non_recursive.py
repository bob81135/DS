def pow(n,m):  #x>0 and y>=0
    ans = 1
    for _ in range(1,m+1):
        ans*=n
    return ans
print(pow(3,3))