from functools import reduce

def Result(x,y):
    if x>y:
        return x
    else:
        return y

l=[100,90,80,200]
ret=reduce(Result,l)
print(ret)