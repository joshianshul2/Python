class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self,a,b):
        c=self.a+self.b
        return c


p=Test(10,20)
print(p.a)
print(p.b)
q=p.add(p.a,p.b)
print("sum =" ,q)
