class Mstack:
    def __init__(self):
        self.stack = []
        print("Hi Mstack")
    def push(self,str1):
        self.stack.append(str1)
    def pop(self):
        return  self.stack.pop()
    def length(self):
        return len(self.stack)
    def __del__(self):
        print(" bye Mstack")

a=Mstack()
b=a
print(b)
print(a)
a.push('abc')
print(a.length())
print(b.length())
del a
#print(a)
#print(b)
a1=Mstack()
b1=Mstack()
a1.push(b1)
print(a1)
print(a1.length())

class MYSU:
    def __init__(self,Su):
        self.Su=Su
    def __lt__(self,Su):
        print("self.Su< other.Su")
    def __gt__(self, Su):
        print("self.Su>other.Su")

a=MYSU(100)
b=MYSU(50)
a>b
a<b
