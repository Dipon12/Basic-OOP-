class A:
    def feature1(self):
        print("feature1 is working...")
    
    def feature2(self):
        print("feature2 is working...")

class B(A):    #class B is Inheriting class A. This is single level inheritance.

    def feature3(self):
        print("feature3 is working...")
    
    def feature4(self):
        print("feature4 is working...")

class C(B): #class C is inheriting class B which is inheriting class A. So class C has feature1,2,3,4,5. This is called Multilevel Inheritance.

    def feature5(self):
        print("feature5 is working...")


class E:  
    def feature6(self):
        print("feature6 is working...")

class F(A,E): #class F is inheriting class A and class E.So class F has feature 1,2,6,7. This is called Multiple Inheritance
    def feature7(self):
        print("feature7 is working...")


c1 = C()

c1.feature1()

c2 = F()

c2.feature6()