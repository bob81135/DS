step = 0
list1 = [0]*6
def fib(n):
    global step
    global list1
    step+=1
    list1[n]+=1
    if(n<2):
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(5),step,list1)