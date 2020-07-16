def GCD(a,b):
    while(a%b!=0):
        buffer = a
        a = b
        b = buffer%b
    return b
print(GCD(1922,24214))