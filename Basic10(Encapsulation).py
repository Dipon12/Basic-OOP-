class Car:

    def __init__(self,speed,color):
        #self.speed = speed
        self.__speed = speed # This means private
        self.__color = color

    def get_speed(self):
        return self.__speed


c1 = Car(200, 'Red')
c1.speed = 300

print(c1.get_speed())