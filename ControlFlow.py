number=1
if number<=10 and number>=1:
    print("good")
else:
    print("bad")

var1=100
if var1:
    print(True)
    print(var1)

var2=0
if var2: #False
    print(False)
    print(var2)
print("Good bye!")

a=int(input('a:'))
if a>0:
    print(a)
else:
    print(None)

score=input("score:")
score=int(score)
if(score>=90 and score<100):
    print("A")
elif(score>=80 and score<90):
    print("B")
else:
    print("C")