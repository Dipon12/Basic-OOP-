class A:
    def __init__(self):
        print("Class A init")

    def feature1(self):
        print("feature1 is working...")
    
    def feature2(self):
        print("feature2 is working...")


class B(A):
    def __init__(self):
        print("Class B init")
        super().__init__()

    def feature3(self):
        print("feature3 is working...")
    
    def feature4(self):
        print("feature4 is working...")


class C:
    def __init__(self):
        print("class C init")

    def feature5(self):
        print("feature5 is working ...")

class D(C,A):

    def __init__(self):
        super().__init__()
        print("class D init")

    def feature5(self):
        print("feature6 is working ...")


    def using_func(self):
        super().feature1()  # Using Function of Super Class

#i1 = B()

i2 = D()
i2.using_func()