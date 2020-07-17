def pow(n,m):
    ans = 1
    for _ in range(1,m+1):
        ans*=n
    return ans
print(pow(3,3))