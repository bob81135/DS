clock = 0
def GCD(a,b):
    global clock
    clock+=1
    if(a%b==0):
        return b
    else:
        return GCD(b,a%b)
print(GCD(1922,24214),clock)