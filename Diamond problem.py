# Diamond problem

class A:
    def method(self):
        print("This is method A")

class B(A):

    def method(self):
        print("This is method B")

class C(A):

    def method(self):
        print("This is method C")

class D(B,C):
    
    def method(self):
        print("This is method D")

# the output will be "This is method D"

# This is method D
obj_D = D()
obj_D.method()

help(obj_D)

# The short will be:
# class first_exc(second_exc,third_exc), fourth_exc
# class D(B,C): = class D(B,C,A)