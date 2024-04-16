# Ex-6.2
# Create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must have two getters getArea() (PI*r^2) and getPerimeter() (2*PI*r) which give both respective areas and perimeter (circumference).

# For help with this class, I have provided you with a Rectangle constructor which you can use as a base example.

# Examples:
# 	circy = Circle(11)
# 	circy.getArea()

# 	# Should return 380.132711084365

# 	circy = Circle(4.44)
# 	circy.getPerimeter()

# 	# Should return 27.897342763877365



import math
class circle:
    def __init__ (self,radius):
        self.radius = radius
    def getarea(self):
        return round(math.pi*self.radius**2)
    def getperimeter(self):
        return round (2*math.pi*self.radius)
circy = circle(11)
print(circy.getarea())
print(circy.getperimeter())










