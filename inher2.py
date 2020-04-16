class A:
    def show(self):
        print("Hello from A")

class B (A):
    def show2(self):
        print("Hello from B")
class C(B):
    def display(self):
      print("Hello from C")

q=A()
q.show()
p=B()
p.show()
p.show2()
r=C()
r.show()
r.show2()
r.display()


