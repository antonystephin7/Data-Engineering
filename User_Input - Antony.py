#Ask the user to enter their name and print a welcome message
name=input('Enter your Name: ')
print(f"Hey, {name} Welcome!!")

#Ask the user to enter their age and print their age
age=int(input("Whats your age: "))
print(f"Im {age} years old")

#Ask the user to enter two numbers and print them
a=int(input('Enter a number1: '))
b=int(input('Enter a number2: '))
print(f"The numbers are {a} and {b}")

#Ask the user to enter their name, age, and city and display all three
name=input("Enter your name: ")
age=int(input("Enter your age: "))
city=input("Enter your city: ")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")

#Ask the user to enter two numbers and calculate their sum
number1=int(input("Enter the number1: "))
number2=int(input("Enter the number2: "))
print(f"The sum of {number1} and {number2} is {number1 + number2}")

#Ask the user to enter the length and breadth of a rectangle and calculate its area
length=int(input("Enter the length: "))
breadth=int(input("Enter the breadth: "))
print(f"The area of a rectangle is {length*breadth}")

#Ask the user to enter the radius of a circle and calculate its area
import math
radius=int(input("Enter the radius of a circle: "))
area=math.pi *(radius**2)
print(f"The area of a circle is {area}")

#Ask the user to enter their marks in three subjects and print the total
english=int(input("Enter your english mark: "))
tamil=int(input("Enter your tamil mark: "))
maths=int(input("Enter your maths mark: "))
print(f"The total marks obtained is {english+tamil+maths}")