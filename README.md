### About Object

Object has two things:
- Attribute/Properties - Basically, Data Regarding Object (If Person is object, then persons height,weight) [Variable of the class]
- Behaviour - Actions that defines what the object does (If Person is object then it dances/Sings) [Methods of the class]

**Class is the design for a Object/Instance.**

### Constructor

In Python, _def init_ method is the **CONSTRUCTOR** method. Constructor is the method that is executed whenever the class is called. It is used to store instance variable. 

 We can think that, each instance is different types of 'variable' of that class. Means, class is the type of instance variable.

 Each object will have their own Variable and Methods.

 **What the Constructor method actually does???**

 Ans: Everytime a instance/object of a class is created, memory is allocated from Heap for that instance/object. But how to determine the size of the instance? Of course it depends on the class which is further depended how much variables are used in that class. That is where Constructor comes to help. It determines the size to take for the instance.

 Every time you create an object it is allocated to new space.


 ## About Variable

 In OOP there are two types of variable:-

 - Instance/Object Variable: It is written inside Constructor method (def __init__). Instance variable is different among different instances. You can change the value of an instance variable and it will affect only one instance, other intances are unharmed.
 - Class/Static Variable: It is written outside Constructor method. This Variable is same in all instances that is created from that class. Changing the value of a class variable will change the value of that variable among all instances of that class.

 
 **NOTE THAT** Namespace is an area where you create and store object/variables. There are two namespaces in OOP:
 - Class Namespace
 - Instance/Object Namespace

Instance Namespace is where the instances are created and Class Namespace is where Blueprints are stored. Class Variables are part of Class Namespace. On the other hand, instance variables are part of the Instance Namespace. Hence, value of the variables are changed as follows: 
 
 ```
 c1 = Car() # c1 is a instance of class Car
 c1.color = "Blue" # Changing a Instance Variable Value

 c2 = Car() 

 Car.wheels = 5 # As variable "wheels" declared in the Class Namespace hence it is called by Class Name instead of Instance name like others. 
 ```
 
 ## About Methods

 There are 3 types of methods in Pyhton OOP:
 - Instance Method : Works with instance variable. Parameter 'Self' is included. 
 - Class Method : Works with class variable. Parameter 'cls' is included.
 - Static Method : Works with neither class variable nor instance variable. 

```
def avg_marks(self):                                 # Instance Method (Bcz its parameter is self. So it works with instance variable)
    return (self.marks1+self.marks2+self.marks3)/3

@classmethod                            #Decorator to indicate that following method is a class method
def getSchool(cls):                         #Class Method. Bcz Parameter is class and works with class variable.
    return cls.grad_school

@staticmethod                            # Decorator to indicate the following method is a static method
def info():                               # Static Method
    return "This is a Static Method"
```

There is also **Accessor Methods** and **Mutator Methods** . Methods that accesses the data(value of the variable) but don't changes it of a class are called **Accessor Methods** and those who changes it are called **Mutator Methods**.


## Accessing Inner Class

To access inner class method you need to write:

`outer_class_name.inner_class_instance_name.inner_class_method_name`
