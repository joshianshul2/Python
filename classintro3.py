class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self,a,b):
        c=self.a+self.b
        return c

    def show(self):
        print(self.a , self.b)
# , is use for sepration operator;
p=Test(10,20)
p.show()
