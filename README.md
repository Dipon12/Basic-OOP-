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


## Inheritance

**See _Basic6(Inheritance).py_ Code**

Lets say, class B is inheriting class A. So:

`class B(A):`

This is called **single level inheritance** .Now if class C inherits class B than:

`class C(B):`

This is called **multilevel level inheritance** . If class F is inheriting class A and class E than:

`class F(A,E):`

This is called **multiple inheritance** . 


## Constructor Inheritance

Suppose there are 2 classes, class A and class B. class B inherits class A. A instance is crearted of class B.

### Situation-1 (class A has __init__ but class B don't)

In such Case, constructor of class A will be executed.

### Situation-2 (class A and class B both have __init__ )

Although both have the constructor, but as instance is created of class B, only __init__ of class B will be executed and __init__ of class B will be ignored.

### Situation-3 (class A and class B both have __init__ but i want to execute __init__ of class A too)

**Use super()**

```
class B(A):
    def __init__(self):
        print("Class B init")
        super().__init__()

OUTPUT:

Class B init
Class A init
```

If order is reversed than:

```
class B(A):
    def __init__(self):
        super().__init__()
        print("Class B init")

OUTPUT:

Class A init
Class B init
```

### Situation-4 

Say, there are two more classes, class C and class D. Both have their own __init__ function. class D inherits class A and class C. As this is a multiple inheritance situation what will happen upon the call of super().__init__() ??? Answer is as follows:

```
class D(A,C):

    def __init__(self):
        super().__init__()
        print("class D init")

    def feature5(self):
        print("feature6 is working ...")

Output: 

class A init
class D init
```

If the parameter order is reversed:

```
class D(C,A):

    def __init__(self):
        super().__init__()
        print("class D init")

    def feature5(self):
        print("feature6 is working ...")

Output: 

class C init
class D init
```

**NOTE THAT** the output is changed. It searches for __init__ function from left to right in the parameter list of class D. This is called **Method Resolution Order(MRO)**.

## Polymorphism

Polymorphism is basically doing the same thing for different type/number of inputs. Say we want to calculate area of a room and hence we declared two methods in the same class which have the same name. If two input is provided then the return would be x\*y from first method if one input is provided the return would be x\*x from second method. But the most important thing is both method have the same name but OOP concept made them different. This is also called Method Overloading.

Another Example is say we have three method named speak(). But if input is Dog then method 1 is executed or if input is Human than method 2 is executed.

Types of Polymorphism:

- Duck Typing

### Duck Typing

If a bird walks like a Duck,swims like a Duck, quacks like a Duck than it is probably a Duck. See _Basic9(DuckTyping).py_

