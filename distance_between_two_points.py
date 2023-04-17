import math

print("Enter the coordinates for first point:\n")
x1 = eval(input("Enter the x axis: "))
y1 = eval(input("Enter the y axis: "))
print("Enter the coordinates for second point:\n")
x2 = eval(input("Enter the x axis: "))
y2 = eval(input("Enter the y axis: "))

distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

print("distance is: ",distance)