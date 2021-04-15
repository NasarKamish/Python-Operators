X = float(input("Enter the first side of your triangle:"))
Y = float(input("Enter the second side of your triangle:"))

answer = (X ** 2) + (Y ** 2)
answer = answer ** (1/2)

print("The third side of your triangle is: " + str(answer))

area = (1/2) * X * Y
print("The area of your triangle is: " + str(area))
print("The area of your triangle in binary is: " + bin(int(area)))
# This code will work finding out the hypotenuse
