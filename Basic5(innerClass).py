class Student:

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):   #This self indicates Student class
        print(self.name , self.roll)
        self.lap.show()  #indicates show function inside Laptop class

    class Laptop:

        def __init__(self):
            self.brand = "ASUS"
            self.cpu = "Ryzen5"
            self.ram = 8

        def show(self):     # This self indicates Laptop class
            print(self.brand , self.cpu , self.ram)



s1 = Student("Dipon" , 9)
s2 = Student("Abu Hena", 5)

s1.show() #show function outside Laptop class
s1.lap.show() #show Function inside Laptop class