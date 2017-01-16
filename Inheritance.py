#Pyhton 은 다중 상속을 지원
class Parent:
    parentAttr = 100
    def __init__(self):
        print('부모 생성자')
    def parentMethod(self):
        print('부모 메소드')
    def setAttr(self,attr):
        Parent.parentAttr=attr
    def getAttr(self):
        print("Parent attribute:", Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print('후손의 생성자')
    def childMethod(self):
        print('후손의 메소드')

c=Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

class MyScore:
    def __init__(self,kor,eng):
        self.kor=kor
        self.eng=eng
    def getTot(self):
        return (self.kor+self.eng)

class MyScore_sub(MyScore):
    def __init__(self,kor,eng,mat):
        self.mat=mat
        super().__init__(kor,eng)
    def getTot(self):
        return (super().getTot()+self.mat)

class MyRes(MyScore_sub):
    def __init__(self,kor,eng,mat,music):
        self.music=music
        super().__init__(kor,eng,mat)
    def getTot(self):
        return (super().getTot()+self.music)
my = MyRes(90,90,90,90)
print(my.getTot())
