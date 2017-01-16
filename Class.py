class MyList:
    def empty(self):
        self.data=[]
    def add(self,x):
        self.data.append(x)
    def getData(self):
        return list(self.data)

my01 = MyList()
my01.empty()
my01.add((list(range(int(1),int(6)))))
print(my01.getData())
print(dir(MyList))