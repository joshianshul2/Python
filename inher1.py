class A:
    def show(self):
      print("Hello from A")

class B (A):
    def show2(self):
     print("Hello from B")

q=A()
q.show()
#q.show2()
p=B()
p.show()
p.show2()

