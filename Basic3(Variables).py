class Car:

    wheels = 4               # Class Variable / Static Variable

    def __init__(self):
        self.color = "Red"               #Instance Variable
        self.company = "BMW"            #Instance Variable



c1 = Car()
c1.color = "Blue" # Changing a Instance Variable Value

c2 = Car() 

Car.wheels = 5 # As variable "wheels" declared in the Class Namespace hence it is called by Class Name instead of Instance name like others. 

print(c1.color, c1.wheels)
print(c2.color, c2.wheels)