class Cdr(object) :
    def __init__(self,x,y):
       self.x=x
       self.y=y
    def distance(self):
      print(self.x*self.y)


s=Cdr(12,13)
s.distance()
