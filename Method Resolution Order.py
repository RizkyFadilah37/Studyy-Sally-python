# Multiple Inheritance

class A:
    def method(self):
        print("This is method A")

class B:
    def method(self):
        print("This is method B")


# Method Resolution Order (MRO)
# MRO is the order in which Python looks for a method in a hierarchy of classes.
# It is also called linearization of a class hierarchy.

# class first_exc(second_exc,third_exc)
class C(A,B):
    pass

# the output will be "This is method A"
obj_C = C()
obj_C.method()


