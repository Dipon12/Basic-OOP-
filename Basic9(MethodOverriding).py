class A:

    def show(self): 
        print("From A...")

class B(A):   # class B inheriting class A

    def show(self):  #This show() method Overriding class A show method
        print("From B...")


i = B()
i.show()