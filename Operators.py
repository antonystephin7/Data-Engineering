#Arithmetic Operators#
#Take two numbers and perform the following
a=10
b=2
print(f"Addition: {a+b}")
print(f"Subtraction: {a-b}")
print(f"Multiplication: {a*b}")
print(f"Division: {a/b}")
print(f"Floor division: {a//b}")
print(f"Modulus: {a%b}")
print(f"Exponentiation: {a**b}")

#Calculate the area and perimeter of a rectangle
length=2
breadth=5
area=length * breadth
perimeter=2*(length + breadth)
print(f"The area of the rectangle is {area}")
print(f"The perimeter of the rectangle is {perimeter}")

#Calculate the total and average of three numbers
number1=10
number2=20
number3=30
total=int(number1+number2+number3)
average=float(total/3)
print(f"Total: {total}")
print(f"Average: {average}")

#Calculate the simple interest
P=5000
R=2
T=10
SI=P*R*T/100
print(f"Simple Interest: {SI}")

#Take a number and calculate its square and cube
number1=5
square=number1**2
cube=number1**3
print(f"Square: {square}")
print(f"Cube: {cube}")

#Take two numbers and find the remainder when the first number is divided by the second
number1=10
number2=2
remainder=number1%number2
print(f"Remainder: {remainder}")

#Assignment Operators#
#Create x = 10 and use += to increase it by 5
x=10
x+=5
print(x)

#Create x = 20 and use -= to decrease it by 7
x=20
x-=7
print(x)

#Create x = 5 and use *= to multiply it by 4
x=5
x*=4
print(x)

#Create x = 17 and use //= with 3
x=17
x//=3
print(x)

#Create x = 10 and use %= with 3
x=10
x%=3
print(x)

#Create x = 2 and use **= with 3
x=2
x**=3
print(x)

#Start with x = 100 and perform at least five different assignment operations
x=100
x+=10
x-=5
x*=2
x/=2
x**=2
print(x)

#Comparison Operators#
#Take two numbers and check whether they are equal
number1=float(input("Enter the number1: "))
number2=float(input("Enter the number2: "))
if number1==number2:
    print("The two numbers are equal.")
else:
    print("The two numbers are not equal.")

#Check whether the first number is greater than the second
number1=float(input("Enter the first number: "))
number2=float(input("Enter the second number: "))
if number1>number2:
    print("The first number is greater than second number")
else:
    print("The first number is not greater than second number")

#Check whether the first number is smaller than the second.
number1=float(input("Enter the first number: "))
number2=float(input("Enter the second number: "))
if number1<number2:
    print("The first number is smaller than second number")
else:
    print("The first number is not smaller than second number")

#Check whether two user-entered numbers are different
number1=float(input("Enter the number: "))
number2=float(input("Enter another number: "))
if number1==number2:
    print("Both the numbers are same")
else:
    print("Both the numbers are different")

#Take a student's mark and check whether it is greater than or equal to 50
english=float(input("Enter your english mark: "))
if english>=50:
    print("You are passed in English")

#Take a person's age and check whether they are 18 or above
age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote!!")

#Compare two strings using == and !=
tamil=float(input("Enter your tamil mark: "))
maths=float(input("Enter your maths mark: "))
if tamil!=maths:
    print("Both marks are different")
if tamil==maths:
    print("Both marks are same")

#Logical Operators#
#Take age as input and check whether the person is between 18 and 60 using and
age=int(input("Enter your age: "))
if age>=18 and age<=60:
    print("You are a major customer!!")

#Check whether a number is either less than 10 or greater than 100 using or
number=float(input("Enter a number: "))
if number<10 or number>100:
    print("The condition is satisfied!!")

#Take a number and check whether it is not equal to 0 using not
number1=int(input("Enter the number: "))
if number1!=0:
    print("The number is not equal to zero.")

#Check whether a student has passed both subjects: Maths ≥ 40 Science ≥ 40
maths=float(input("Enter your maths mark: "))
science=float(input("Enter your science mark: "))
if maths>=40:
    print("Congrats!! You are passed in Maths!!")
if science>=40:
    print("Congrats!! You are passed in Science!!")

#Check whether a person can vote using: Age ≥ 18 Citizen = True
age=int(input("Enter your age: "))
citizen=bool(input("Are you an Indian citizen: "))
if age>=18 and citizen==True:
    print("You are eligible for voting!!")

#Check whether a number is between 10 and 50 using logical operators
price=float(input("Enter the price: "))
if price>10 or price<50:
    print("The given condition is satisfied!!")

#Bitwise Operators#
#Find the result of a & b
a=10
b=6
print(a&b)
print(a|b)
print(a^b)
print(~a)

#Take two integers from the user and perform &, |, and ^
c=20
d=10
print(c&d)
print(c|d)
print(c^d)

#Take a number from the user and apply the ~ operator
f=int(input("Enter any number: "))
result=~f
print(f"{result}")

#Predict the output before executing: print(5 & 3)
a=5
b=3
print(a&b)
print(a|b)
print(a^b)
print(~a)