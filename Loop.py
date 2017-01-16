i=1
while i<=10:
    print(i)
    i+=1

i=104
while i>100:
    print(i)
    i-=2
else:
    print("Loop end")

print("\n===========================")
for index, value in enumerate(['banana','apple','pear','quince']):
    print(index,value)

print("\n===========================")
my_str=['banana','apple','pear','quince']
print(list(enumerate(my_str)))

print("\n===========================")
for index,item   in enumerate(my_str,start=1):
    print(index,item)

print("\n===========================")
dic={'x':1,'y':2,'z':3}
for key,value in enumerate(dic):
    print(key,':=>',value,type(key))
print("\n===========================")

for index,item   in enumerate(my_str,start=1):
    print(index,item)
print("\n===========================")

r=list(range(0,20,4))
print(r)
print("\n===========================")

fruit=['apple','watermelon','peach']
for i in enumerate(fruit,100):
        print(i)
print("\n===========================")
for i in range(1,10):
    if i>5 :
        break
    else :
        print(i)
print("\n===========================")
for i in range(1,10):
    if i%2==0 :
            continue
    print(i)
print("\n===========================")
#for i in range(1,10):
#    for j in range(1,9):
#        print("$d*$d=\t"%(i,j),i*j)
print("\n===========================")
while True:
    line=input('input>')
    if line=='done':
        break
    print(line)
print('Done!')
print("\n===========================")
passwdlist=["123","456"]
valid=False
count=3
while count>0:
    res=input("enter password:")
    for eachPass in passwdlist:
        if res==eachPass:
            valid=True
            break
    if not valid:
        print("invalid input")
        count-=1
        continue
    else:
        break

print("\n===========================")
while True:
    res=input("Enter word:")
    if res=='quit':
        break
    if len(res)<5:
        print("Too small")
    else :
        print(res)
    continue
