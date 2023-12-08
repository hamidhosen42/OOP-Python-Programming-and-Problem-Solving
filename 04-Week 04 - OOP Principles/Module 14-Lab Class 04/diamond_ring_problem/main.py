
# !"""diamond_ring_is_a_problem"""

class A:
    def print_some(self):
        print("I am A")

class B(A):
    def print_some(self):
        print("I am B")

class C(A):
    def print_some(self):
        print("I am C")

class D(B,C):
    # def print_some(self):
    #     print("I am D")
    pass

obj1 = A()
obj2 = B()
obj3 = C()
obj4 = D()

obj1.print_some()
obj2.print_some()
obj3.print_some()
obj4.print_some()