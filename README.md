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
 