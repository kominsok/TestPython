class My:
    def __init__(self):
        self.x=0
    @property
    def mFun(self):
        return self.x
    @mFun.setter
    def mFun(self,x):
        self.x=x
    @classmethod
    def class_Fun(cls,x):
        print("class_Fun(%s%d)"%(cls,x))
    @staticmethod
    def static_Fun(x):
        print("static_Fun(%d)"%x)

a=My()
a.mFun=int(100)
print(a.mFun)
My.class_Fun(10)
a.class_Fun(20)
My.static_Fun(10)

class Doitch08():
    def __init__(self,temperature=0):
        self._temperature=temperature
    def to_value(self):
        return (self.temperature*1.8)+32
    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self,value):
        self._temperature=value

v=Doitch08()
for i in range(10,15):
    v.temperature=i
    print(str(v.to_value()))