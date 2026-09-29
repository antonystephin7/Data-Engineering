#Convert the string "100" into an integer
str_number="100"
int_number=int(str_number)

#Convert the integer 50 into a float
int_number=50
float_number=float(int_number)

#Convert the integer 100 into a string
int_number=100
str_number=str(int_number)

#Convert the string "25.75" into a float
str_number="25.75"
float_number=float(str_number)

#Take two numbers from the user and perform addition after converting them to integers
number1=input("Enter the number1: ")
number2=input("Enter the number2: ")
result=int(number1) + int(number2)
print(f"The sum of {number1} and {number2} is {result}")

#Take the user's age as input and convert it into an integer
age=input("Enter your age: ")
int_age=int(age)
print(f"My age is {int_age}")

#Take a decimal number as input and convert it into an integer. Observe the result
price=55.00
int_price=int(price)
print(int_price)

#Take an integer as input, convert it into a float, and print its type
user_input=int(input("Enter a number: "))
float_int=float(user_input)
print(type(float_int))