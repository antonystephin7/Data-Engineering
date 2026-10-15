#if Condition#
#Take a number from the user. Print "Positive" if the number is greater than 0
user_input=int(input("Enter a number: "))
if user_input>0:
    print("Output: The number is positive!!")

#Take a number and print "Even" if it is divisible by 2
number=int(input("Enter any number: "))
if number%2==0:
    print("Output: The entered number is even!!")

#Take a person's age and print "Eligible to vote" if age is 18 or above
age=int(input("Enter your age: "))
if age>=18:
    print("Hurrah!! You are eligible to vote!!")

#Take a student's mark and print "Pass" if the mark is 40 or above
mark=int(input("Enter your mark: "))
if mark>=40:
    print("Congrats!! You are passed!!")

#Take a number and print "Greater than 100" if it is greater than 100
number=int(input("Enter any number: "))
if number>100:
    print("Output: The number is greater than 100")

#Take a number and print "Divisible by 5" if it is divisible by 5
number=int(input("Enter any number: "))
if number%5==0:
    print("The entered number is divisible by 5")

#Take a salary and print "High Salary" if salary is greater than 50,000
salary=int(input("Enter your salary: "))
if salary>50000:
    print("High Salary!!")

#Take a temperature and print "Hot" if the temperature is greater than 30
temperature=float(input("Enter the temperature: "))
if temperature>30:
    print("The temperature is hot!!")

#Take a number and print "Multiple of 10" if it is divisible by 10
number=int(input("Enter any number: "))
if number%10==0:
    print("The entered number is divisible by 10")

#Take a string and print "Python" if the entered string is "Python"
str=str(input("Enter the string: "))
if str=="Python":
    print("Python")

#if-else Condition#
#Take a number and check whether it is even or odd
number=int(input("Enter the number: "))
if number%2==0:
    print("The number is even!!")
else:
    print("The number is odd!!")

#Take a number and check whether it is positive or negative
number=int(input("Enter the number: "))
if number>0:
    print("The number is positive!!")
else:
    print("The number is negative!!")

#Take a student's mark and display Pass or Fail
mark=int(input("Enter your mark: "))
if mark>=50:
    print("Congrats!! You secured in the exam!! ")
else:
    print("Oops!! You failed!!")

#Take a person's age and display Adult or Minor
age=int(input("Enter your age: "))
if age>=18:
    print("You are an adult!!")
else:
    print("You are a minor!!")

#Take two numbers and print the greater number
number1=float(input("Enter the number1: "))
number2=float(input("Enter the number2: "))
if number1>number2:
    print(f"{number1} is greater than {number2}")
elif number2>number1:
    print(f"{number2} is greater than {number1}")

#Take two numbers and check whether they are equal or not equal
num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
if num1==num2:
    print("Both the numbers are equal.")
else:
    print("Both the numbers are not equal.")

#Take a number and check whether it is divisible by 5 or not
number=int(input("Enter the number: "))
if number%5==0:
    print("The given number is divisible by 5.")

#Take a username from the user. If it is "admin", print "Welcome Admin", otherwise print "Invalid User"
username=str(input("Enter the username: "))
if username=='admin':
    print("Welcome Admin!!")
else:
    print("Invalid User")

#Take a password from the user. If the password is "python123", print "Login Successful", otherwise print "Incorrect Password"
password=str(input("Enter your password: "))
if password=='python123':
    print("Login Successful!!")
else:
    print("Incorrect Password!!")

#Take a student's attendance percentage. If it is 75 or above, print "Eligible for Exam", otherwise print "Not Eligible"
attendance=str(input("Enter the attendance: "))
if attendance>=75:
    print("You are eligible for exam.")
else:
    print("Not eligible for exam.")

#if-elif-else Condition#
#Take a number and display: "Positive" if greater than 0 "Negative" if less than 0 "Zero" if equal to 0
num=float(input("Enter the number: "))
if num>0:
    print("The entered number is positive!!")
elif num==0:
    print("The entered number is zero!!")
elif num<0:
    print("The entered number is negative!!")

#Take a student's mark and display: A → 90–100 B → 75–89 C → 60–74 D → 40–59 F → below 40
mark=float(input("Enter your mark: "))
if mark>90 and mark<=100:
    print("Grade: A")
elif mark>75 and mark<=89:
    print("Grade: B")
elif mark>60 and mark<=74:
    print("Grade: C")
elif mark>40 and mark<=59:
    print("Grade: D")
elif mark<40:
    print("Grade: F")

#Take a person's age and display: "Child" → below 13 "Teenager" → 13–19 "Adult" → 20–59 "Senior Citizen" → 60 or above
age=int(input("Enter your age: "))
if age<13:
    print("You are a child!!")
elif age>=13 and age<=19:
    print("You are a teenager!!")
elif age>20 and age<=59:
    print("You are an adult")
elif age>=60:
    print("You are a senior citizen")

#Take a number and check whether it is: Positive Even, Positive Odd, Negative Even, Negative Odd, Zero
number = int(input("Enter a number: "))
if number == 0:
    print("The number is zero.")
elif number > 0:
    if number % 2 == 0:
        print("The number is positive even.")
    else: 
        print("The number is positive odd.")
else:
    if number % 2 == 0:
        print("The number is negative even.")
    else:
        print("The number is negative odd.")

#Take a temperature and display: "Cold" → below 20 "Normal" → 20–30 "Hot" → above 30
temperature=float(input("Current temperature is: "))
if temperature < 20:
    print("The temperature is cold.")
elif temperature >=20 and temperature < 30:
    print("The temperature is normal.")
elif temperature >=30:
    print("The temperature is hot.")

#Take a month number and display the month name
month=int(input("Enter the month number: "))
if month==1:
    print("Its January!")
elif month==2:
    print("Its February!")
elif month==3:
    print("Its March!")
elif month==4:
    print("Its April!")
elif month==5:
    print("Its May!")
elif month==6:
    print("Its June!")
elif month==7:
    print("Its July!")
elif month==8:
    print("Its August!")
elif month==9:
    print("Its September!")
elif month==10:
    print("Its October!")
elif month==11:
    print("Its November!")
elif month==12:
    print("Its December!")
else:
    print("Invalid month")

#Take a number from 1 to 7 and display the corresponding day
day=int(input("Enter the day number: "))
if day==1:
    print("Its Monday!")
elif day==2:
    print("Its Tuesday!")
elif day==3:
    print("Its Wednesday!")
elif day==4:
    print("Its Thursday!")
elif day==5:
    print("Its Friday!")
elif day==6:
    print("Its Saturday!")
elif day==7:
    print("Its Sunday!")
else:
    print("Invalid Day")

#Take a student's percentage and display
percentage=int(input("Enter your percentage: "))
if percentage<=100 and percentage>=90:
    print("You secured Distinction.")
elif percentage<=89 and percentage>=75:
    print("You secured First Class.")
elif percentage<=74 and percentage>=60:
    print("You secured Second Class.")
elif percentage<=59 and percentage>=40:
    print("You are Passed.")
elif percentage<40:
    print("You are failed.")
else: 
    print("Invalid Mark")

#Take a person's age and calculate the ticket category:
age=int(input("Enter your age: "))
if age < 5:
    print("ELigible for free ticket!!")
elif age >=5 and age <=12:
    print("Pay for Child Ticket!!")
elif age >= 13 and age <=59:
    print("Pay for Adult Ticket!!")
elif age >= 60:
    print("Pay for Senior Citizen Ticket!!")
else: 
    print("Invalid age")

#Nested Conditions#
#Take a number. First check whether it is positive. If positive, check whether it is even or odd.
num=float(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive.")
    if num % 2 == 0:
        print(f"{num} is positive even.")
    else:
        print(f"{num} is positive odd.")
else:
    print(f"{num} is not a positive number.")

#Take a student's mark. If the student has passed, check whether the mark is above 75
mark=int(input("Enter your mark: "))
if mark > 50:
    print("You are passed.")
    if mark > 75:
        print("You scored above 75.")
    else:
        print("You scored below 75.")
else:
    print("You are failed.")

#Take age and citizenship status. Check whether the person is eligible to vote only when: Age ≥ 18 Citizen = True
age=int(input("Enter your age: "))
citizen=input("Are you an indian citizen: ")
if age >= 18:
    if citizen == "True":
        print("Super Cool! You are eligible to vote..")
    else:
        print("Oops! Voting is eligible only for Indians. You are not eligible to vote ..")
else:
    print("Oops! You are not eligible to vote..")

#Take username and password. Check whether the username is correct first, then check the password.
user="antony"
pswrd = "123"

username=input("Enter your username: ")
password=input("Enter your password: ")

if username == user:
    if password == pswrd:
        print("Login successful!")
    else:
        print("Incorrect Password!")
else:
    print("Incorrect username!")

#Take three numbers and find the largest number using nested if conditions
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))

if num1 >= num2:
    if num1 >= num3:
        print(f"{num1} is the largest number.")
    else:
        print(f"{num3} is the largest number.")
else:
    if num2 >= num1:
        if num2 >= num3:
            print(f"{num2} is the largest number.")
        else:
            print(f"{num3} is the largest number.")

#Electricity Bill - Take units consumed and calculate:
units=float(input("Enter the units consumed: "))

if units > 0 and units <= 100:
    print(f"Bill Amount for {units} units is Rs. {units * 2}")
elif units >= 101 and units <= 200:
    print(f"Bill Amount for {units} units is Rs. {units * 3}")
elif units >= 201 and units <= 500:
    print(f"Bill Amount for {units} units is Rs. {units * 5}")
elif units >=500:
    print(f"Bill Amount for {units} units is Rs. {units * 7}")
else:
    print("Incorrect units.")

#ATM Withdrawal Take account balance and withdrawal amount. Check:
balance=float(input("Enter your Bank Balance: "))
withdrawal=float(input("Enter the amount to be withdrawn: "))
    
if withdrawal <= balance:
        print("The withdrawal amount is valid.")
        print(f"Total Balance: {balance}")

elif withdrawal > balance:
    print(f"Insufficient Amount. Enter an amount lesser than {balance}")

else:
    print("Invalid Amount")

#Login System. Take: username, password. Check whether both are correct and display an appropriate message.
username ="antony"
password = 'a123'

username_input = input("Enter the username: ")
password_input = input("Enter the password: ")

if username_input == username:
    if password_input == password:
        print("Login Successful.")
    else:
        print("Invalid password.")
else:
    print("Invalid username.")

#Take two numbers and an operator:
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

operator = input("Enter the operator: ")

if operator == '+':
    print(f"The sum of {num1} and {num2} is {num1 + num2}.")

elif operator == '-':
    print(f"The subtraction of {num1} and {num2} is {num1 - num2}.")

elif operator == '*':
    print(f"The multiplication of {num1} and {num2} is {num1 * num2}.")

elif operator == '/':
    print(f"The division of {num1} and {num2} is {num1 / num2}.")

else:
    print("Invalid operator.")

#Take marks for three subjects, calculate the average, and display the grade using if-elif-else
english = int(input("Enter your english mark: "))
tamil = int(input("Enter your tamil mark: "))
maths = int(input("Enter your maths mark: "))

average = (english + tamil + maths)/3

if average >= 90:
    print("Grade: A")

elif average >=75:
    print("Grade: B")

elif average >=60:
    print("Grade: C")

elif average >=50:
    print("Grade: D")

elif average < 50:
    print("Grade: Fail")

else:
    print("Invalid marks entered.")