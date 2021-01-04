class Student:

    grad_school = "Chittagong University of Engineering and Technology"

    def __init__(self,marks1,marks2,marks3): # Constructor Method
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    
    def avg_marks(self):                                 # Instance Method (Bcz its parameter is self. So it works with instance variable)
        return (self.marks1+self.marks2+self.marks3)/3

    @classmethod                            #Decorator to indicate that following method is a class method
    def getSchool(cls):                         #Class Method. Bcz Parameter is class and works with class variable.
        return cls.grad_school
    
    @staticmethod                            # Decorator to indicate the following method is a static method
    def info():                               # Static Method
        return "This is a Static Method"


s1 = Student(10,20,30)
s2 = Student(30,40,50)


print(s1.getSchool())
print(Student.getSchool())

print(s1.info() )   
print(Student.info() )    # This also works as info() is a class method
