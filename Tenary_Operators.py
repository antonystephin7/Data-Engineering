#Take a number from the user and print "Even" if it is even, otherwise "Odd".
num = int(input("Enter the number: "))
result = "Even" if num%2 == 0 else "Odd"
print(result)

#Take a number and print "Positive" if it is greater than 0, otherwise "Negative".
number = int(input("Enter a number: "))
print("Positive" if number > 0 else "Negative")

#Take a number and print "Zero" if it is 0, otherwise "Non-zero".
num=int(input("Enter a number: "))
print("Zero" if num == 0 else "Non-zero")

#Take a person's age and print "Adult" if age is 18 or above, otherwise "Minor".
age=int(input("Enter your age: "))
print("Adult" if age >= 18 else "Minor")

#Take a number and print "Greater than 50" if it is greater than 50, otherwise "50 or less".
number = int(input("Enter any number: "))
print("Greater than 50" if number > 50 else "50 or less")

#Take two numbers and print the larger number using a ternary operator.
num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
print(f"{num1} is larger" if num1 > num2 else f"{num2} is larger.")

#Take two numbers and print the smaller number using a ternary operator.
num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
print(f"{num1} is smaller" if num1 > num2 else f"{num2} is smaller.")

#Take a student's mark and print "Pass" if the mark is 40 or above, otherwise "Fail".
mark = int(input("Enter your mark: "))
print("Pass" if mark >=40 else "Fail")

#Take a number and print "Divisible by 5" if it is divisible by 5, otherwise "Not divisible by 5".
number = int(input("Enter a number: "))
print("Divisible by 5" if number%5 == 0 else "Not divisible by 5")

#Take a number and print "Multiple of 10" or "Not a multiple of 10".
number = int(input("Enter a number: "))
print("Multiple by 10" if number%10 == 0 else "Not a multiple of 10")

#Take two numbers and print whether they are equal or not equal
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

print("Equal" if num1 == num2 else "Not equal")

#Take a person's age and print: "Child" if age < 13 "Teenager" otherwise.
age = int(input("Enter your age: "))
print("Child" if age < 13 else "Teenager")

#Take a number and print "Positive Even" or "Not Positive Even".
number = int(input("Enter a number"))
print("Positive Even" if number % 2 == 0 else "Not Positive Even")

#Take two numbers and print the maximum using a ternary operator
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

print(f"{num1} is maximum" if num1 > num2 else f"{num2} is maximum")

#Take three numbers and find the largest number using nested ternary operators.
a = int(input("Enter the num1: "))
b = int(input("Enter the num2: "))
c = int(input("Enter the num3: "))

largest = (a if a>c else c) if a>b else (b if b>a else c)
print(f"Largest number is {largest}")

#Take three numbers and find the smallest number using nested ternary operators.
a = int(input("Enter a number1: "))
b = int(input("Enter a number2: "))
c = int(input("Enter a number3: "))

smallest = (a if a<b else b) if a<c else ( c if c<b else b)
print(f"Smallest number is {smallest}")

#Take a student's mark and display: "Pass" if ≥ 40 "Fail" otherwise.
mark = int(input("Enter the mark: "))
print("Pass" if mark >= 40 else "Fail")

#Take a temperature and print: "Hot" if temperature > 30 "Normal" otherwise
temperature = float(input("Enter the temperature: "))
print("Hot" if temperature>30 else "Normal")

#Take a salary and print: "High Salary" if salary ≥ 50,000 "Low Salary" otherwise
salary = float(input("Enter your salary: "))
print("High Salary" if salary >= 50000 else "Low Salary")

#Take a number and determine whether it is even and positive using a ternary operator.
number = int(input("Enter the number: "))
print("Even positive" if number % 2 == 0 else "Not an even positive")

#Convert if-else to Ternary
#26
age = 20
print("Eligible" if age>=18 else "Not Eligible")

#27
num = 7
print("Even" if num%2==0 else "Odd")

#28
a = 10
b = 20
print("a" if a>b else "b")

#29
marks = 75
print("Pass" if marks >= 50 else "Fail")

#30
num = -5
print("Positive" if num >= 0 else "Negative")

#Find the largest of three numbers using nested ternary operators.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Entert the third number: "))

largest = (a if a>b else b) if a>c else (c if c>a else c)
print(f"Largest number: {largest}")

#Find the smallest of three numbers using nested ternary operators.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Entert the third number: "))

smallest = (a if a<b else b) if a<c else (c if c<a else c)
print(f"Smallest number: {smallest}")

#Check whether a number is positive, negative, or zero using nested ternary operators.
num = int(input("Enter the number to be checked: "))

result = "Positive" if num > 0 else ("Zero"if num == 0 else "Negative")
print(result)

#Take a student's mark and display "Distinction" if ≥ 75, otherwise "Pass" if ≥ 40, otherwise "Fail".
mark = int(input("Enter your marks: "))

result = "Distinction" if mark >= 75 else ("Pass" if mark >= 40 else "Fail")
print(result)

#Take a person's age and display: Child, Teenager, Adult, or Senior Citizen using nested ternary operators.
age = int(input("Enter your age: "))

category = "Child" if age < 13 else ("Teenager" if age < 18 else ("Adult" if age < 60 else "Senior Citizen"))
print(f"Age Category: {category}")