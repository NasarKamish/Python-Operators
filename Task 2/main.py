numbers = [2, 56, 12, 67, 1000, 32, 89, 29, 44, 39, 200, 11, 21]
X = max(numbers)
Y = min(numbers)

answer = (X ** 2) - (Y ** 2)
answer = answer ** (1/2)

print("The third side of your triangle is: " + str(answer))

"""This takes the highest as a hypotenuse and makes the smallest a side"""
