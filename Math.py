from random import  *
from decimal import *

print(random())
print(uniform(1,100))
print(randint(1,100))
print(choice("1234567890ascaweqweq"))
sample_list=["python","java","c++","random","spring"]
print(shuffle(sample_list))
print(sample_list)

print(getcontext())
getcontext().prec=28
print(Decimal(1)/Decimal(7))

m=Context(prec=60,rounding=ROUND_HALF_DOWN)
setcontext(m)
print(Decimal(1)/Decimal(7))