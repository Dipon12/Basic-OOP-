class Person:
    def __init__(self):

        self.Fname = "Dipon"
        self.Lname = "Talukder"

    def printer(self):
        print(f"{self.Fname}  {self.Lname}")


i1 = Person()
i2 = Person()

i1.Fname = "Srijon" # Name changed after acquiring the class variable

print(i1.Fname) # This is how a class variable is called
print(i2.Fname)

i1.printer() # This is how a class method is called
i2.printer()