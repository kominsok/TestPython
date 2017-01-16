def even(x):
    return (x%2==0)
lst=range(10)
print(list(filter(even,lst)))

#lamda
def hab(a,b,c):
    return a+b+c

hap01 = lambda a,b,c:a+b+c
print(hap01(10,20,30))

f=lambda x:x+2
a=f(1)
print(a)

min=(lambda x,y:x if x<y else y)
print(min(100,200))

lambda_a= [(1,'one'),(2,'two'),(3,'three'),(4,'four')]
lambda_a.sort(key=lambda a:a[1])
print(lambda_a)

#filter
print(list(filter(lambda x:x%2==0,range(10))))

#map
print(list(map(lambda a:a*2,[1,2,3,4])))

#reduce
from functools import  reduce
print(reduce(lambda x,y:x+y,range(1,11)))

#recursive
def sum_n(n):
    if n==0:
        return 0
    else:
        return n+sum_n(n-1)

print(sum_n(3))


def fahrenheit(t):
    return t*9/5+32

for t in (22.6,123,23423,123):
    print(t,"C : ",fahrenheit(t),"F")