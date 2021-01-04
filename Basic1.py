class Computer:

    def __init__(self,cpu,ram): # This is Constructor. 'self' indicates that particular instance, it is called for.
        self.cpu = cpu           # Not necessery that name has to be same.
        self.ram = ram

    def config(self):
        print(f"{self.cpu}   {self.ram}")


com1 = Computer('i5','16GB')
com2 = Computer('Ryzen','8GB')

#Computer.config(com1)

com1.config()
com2.config()