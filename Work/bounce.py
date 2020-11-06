# bounce.py
#
# Exercise 1.5
number = 0
height = 100

while number <= 10:
    number = number + 1
    height = height * ( 3 / 5)
    print(number, end=' ')
    print(round(height, 4))
