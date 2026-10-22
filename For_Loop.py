#Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

#Print numbers from 10 to 1.
for i in reversed(range(1,11)):
    print(i)

#Print all numbers from 1 to 20.
for i in range(1,21):
    print(i)

#Print all even numbers from 1 to 20.
for i in range(2,21,2):
    print(i)

#Print all odd numbers from 1 to 20.
for i in range(1,21,2):
    print(i)

#Print multiples of 5 from 5 to 50.
for i in range(5,51,5):
    print(i)

#Print numbers from 20 to 50.
for i in range(20,51):
    print(i)

#Print numbers from 100 to 110.
for i in range(100,111):
    print(i)

#Print the first 10 natural numbers.
for i in range(1,11):
    print(i)

#Print the first 10 whole numbers.
for i in range(0,11):
    print(i)

#Using range()
#Use range() to print numbers from 1 to 10.
for number in range(1,11):
    print(number)

#Use range() to print even numbers from 2 to 20.
for i in range(2,21,2):
    print(i)

#Use range() to print odd numbers from 1 to 19.
for i in range(1,21,2):
    print(i)

#Print numbers from 10 to 50 with a step of 5.
for i in range(10,51,5):
    print(i)

#Print numbers from 50 to 10 in descending order.
for i in reversed(range(10,51)):
    print(i)

#Print multiples of 3 from 3 to 30.
for i in range(3,31,3):
    print(i)

#Print multiples of 7 from 7 to 70.
for i in range(7,71,7):
    print(i)

#Print numbers from 1 to 100 with a step of 10.
for i in range(1,101,10):
    print(i)

#Print the square of numbers from 1 to 10.
for number in range(1,11):
    print(f"The square of {number} is {number ** 2}.")

#Print the cube of numbers from 1 to 10.
for number in range(1,11):
    print(f"The cube of {number} is {number ** 3}.")

#Find the sum of numbers from 1 to 10.
total=0
for i in range(1,11):
    total+=i
print(f"The sum of numbers from 1 to 10 is {total}.")

#Find the sum of numbers from 1 to 100.
total=0
for i in range(1,101):
    total+=i
print(f"The sum of numbers from 1 to 100 is {total}.")

#Find the sum of all even numbers from 1 to 50.
total=0
for i in range(2,51):
    total+=i
print(f"The sum of all even numbers from 2 to 50 is {total}.")

#Find the sum of all odd numbers from 1 to 50.
total=0
for i in range(1,51):
    total+=i
print(f"The sum of all odd numbers from 2 to 50 is {total}.")

#Print the multiplication table of 5.
for i in range(1,11):
    print(f"5 * {i} = {5 * i}")

#Ask the user for a number and print its multiplication table from 1 to 10.
num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{i} * {num} = {i * num} ")

#Ask the user for a number n and calculate the sum from 1 to n
n=int(input("Enter a number: "))
total=0
for i in range(1,n+1):
    total += 1
    print(f"The sum of 1 and {n} is {total} ")

#Find the factorial of a number using a for loop.
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Negative numbers cannot have factorials.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1,num +1):
        factorial *= 1
    print(f"The factorial of {num} is {factorial}")

# Print numbers from 1 to 50 that are divisible by 5.
for i in range(1,51):
    if i%5 == 0:
        print(i)

#Print numbers from 1 to 100 that are divisible by both 3 and 5.
for i in range(1,51):
    if i%3 == 0 and i%5 == 0:
        print(i)

#Print numbers from 1 to 100 that are not divisible by 2.
for i in range(1,101):
    if i%2 != 0:
        print(i)

#Count how many even numbers exist between 1 and 100.
count = 0
for i in range(2,101):
    if i%2 == 0:
        count += 1
print(f"The number of even numbers between 1 and 100 is {count}.")

#Count how many odd numbers exist between 1 and 100.
count = 0
for i in range(1,101):
    if i%2 != 0:
        count += 1
print(f"The number of odd numbers between 1 and 100 is {count}.")

#Find the largest number among numbers from 1 to 20.

#Find the sum of numbers divisible by 3 between 1 and 100.
total = 0
for i in range(1,101):
    if i % 3 == 0:
        total += i
print(f"The sum of numbers divisible by 3 between 1 and 100 is {total}.")

#Print numbers between 1 and 100 that are divisible by 7 but not by 5.
for i in range(1,101):
    if i % 7 == 0 and i % 5 != 0:
        print(i)

#Print each character of "PYTHON" on a separate line.
for char in "PYTHON":
    print(char)

#Count the number of characters in a string using a for loop.
for name in "antony":
    print(name)

#Count the number of vowels in a string.
name = "antony"
vowels = "aeiouAEIOU"
count = 0
for char in name:
    if name in vowels:
        count = 1
print(f"Number of vowels: {count}")

#Count the number of consonants in a string.

#Print only the vowels from a given string.
name = "Lohitha"
vowels = "aeiouAEIOU"
for char in name:
    if char in vowels:
        print(char, end = "")

#Print only the digits from a string such as "abc123xyz45"
text = "abc123xyz45"
for char in text:
    if char.isdigit():
        print(char, end = "")

#Count how many times the letter "a" appears in a string.
name = "antony amala stephin"
count = 0
for char in name:
    if char == 'a':
        count += 1
print(count)

#Reverse a string using a for loop.
role = "data"
for i in reversed(role):
    print(i, end='')

#Print each character along with its position.
name = "antony"
for index, char in enumerate(name):
    print(f"Position {index} = {char}")

#Pattern Programs
for i in range(1,6):
    print("*" * i)

for i in reversed(range(1,6)):
    print("*" * i)

for i in range(1,6):
    for j in range(1, i):
        print(j, end = " ")
    print(i)

for i in range(1,6):
    print(str(i) * i)

for i in range (1,6):
    print("*" * 5)

#Print multiplication tables from 1 to 5.
multiplication = 1
for i in range(1,12):
    row = " "
    for j in range(1,6):
        multiplication = j * i
        print(f"The multiplication of {j} * {i} = {multiplication}")

#. Print numbers in this format: 1 2 3 4 5
for i in range(1,4):
    for j in range(1,6):
        print(j, end=" ")
    print(i)

#Print a 5 × 5 star pattern.
for i in range(1,6):
    for j in range(1,6):
        print("*",end = "")
    print(i)

# Print this pattern:
for i in range(1,4):
    for j in range(1,4):
        print(j, end=" ")
    print(i)

#Print multiplication tables from 2 to 10.
multiplication = 1
for i in range(2,11):
    print(f"--Table of {i}--")
    for j in range(1,10):
        multiplication = i * j
        print(f"{j} * {i} = {multiplication}")

#Ask the user for n and print numbers from 1 to n.
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(i)

# Ask the user for n and print all even numbers up to n.
n = int(input("Enter a number: "))
for i in range(2, n+1, 2):
    print(i)

#Ask the user for n and print all odd numbers up to n.
n = int(input("Enter a number: "))
for i in range(1, n+1, 2):
    print(i)

#Ask the user for n and calculate its factorial.
n = int(input("Enter a number: "))
factorial = 1

if n < 0:
    print("Factorial cannot be executed for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    for n in range(1,n+1):
        factorial *= n
    print(f"Factorial of {n} is {factorial}.")

#Ask the user for a number and print its multiplication table
n = int(input("Enter a number: "))
multiplication = 1

for i in range(1, 11):
    multiplication = i * n
    print(f"{i} * {n} = {i * n}")

#Ask the user for 5 numbers and calculate their sum.
sum = 0
print("Enter any 5 numbers ")
for i in range(1,6):
    num = int(input(f"Enter the number{i}: "))
    sum += num
print(f"The sum of the given numbers is {sum}")

# Ask the user for 5 numbers and find the largest number.
largest_number = int(input("Enter the number1: "))
for i in range(2,6):
    num = int(input(f"Enter the number{i}: "))
    if num > largest_number:
        largest_number = num
print(f"The largest number is {largest_number}")
