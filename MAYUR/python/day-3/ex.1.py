# Write a Program that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points.



import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

distance = calculate_distance(x1, y1, x2, y2)
print("Length of the line segment connecting the two points:", distance)
