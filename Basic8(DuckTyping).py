class PyCharm:

    def execute(self):
        print("Compiled...")
        print("Executed...")



class VStudio:

    def execute(self):

        print("Spell Check...")
        print("Convention Check...")
        print("Compiled...")
        print("Executed...")


class Laptop:

    def code(self,ide):
        ide.execute()


#ide = PyCharm()
ide = VStudio()

"""
As long as the passed parameter (in this case variable 'ide') has the method execute() it will provide result. Although they 
have the same name execute() and called inside same method 'code()' the parameter that is passed divided them. Hence it is
called Polymorphism.
"""



lap1 = Laptop()

lap1.code(ide)

