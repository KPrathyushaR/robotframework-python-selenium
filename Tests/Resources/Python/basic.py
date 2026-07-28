# # Topic 1: Variables
# name = "Prathyusha"
# experience = 6
# salary = 1200000

# # Topic 2: Data Types
# name = "John"          # str
# age = 25               # int
# salary = 25000.50      # float
# is_employee = True     # bool

# # Check the type:
# print(type(name))
# print(type(age))
# print(type(salary))
# print(type(is_employee))

# # Topic 3: Input
# name = input("Enter your name: ")
# print("Hello", name)

# # Integer input
# age = int(input("Enter age: "))
# print(age)

# # Topic 4: Operators
# a = 20
# b = 5

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)

# # Topic 5: Conditions
# age = int(input("Enter age: "))

# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")

# # Topic 6: Loops
# # For loop

# for i in range(1,6):
#     print(i)

# # While loop
# i=1
# while i<=5:
#     print(i)
#     i=i+1
"""    
Coding Practice
Solve these without looking at the answers:
1. Print Hello World
2. Add two numbers
3. Swap two numbers
4. Find the largest of three numbers
5. Check even or odd
6. Find factorial
7. Reverse a string
8. Check palindrome
9. Count vowels
10. Print multiplication table

Answers:
"""

# print("Hello World")

# a=10
# b=20
# print(a+b)

# x=10
# y=20
# print(f"Before swapping the {a} and {b}")
# x,y=y,x
# print(f"After Swapping the {a} and {b}")

# number=[10,20,30]
# print(max(number))
# #using the largest number without max()
# largest=number[0]
# for num in number:
#   if num >largest:
#      largest = num
# print(largest)

# even_odd=int(input("Enter the number:"))
# if even_odd % 2 == 0:
#   print("Even Number")
# else:
#   print("Odd Number")

# number1=int(input("Enter the factorial number:"))
# fact=1
# for i in range(1, number1):
#    fact*=i
# print("Factorial Number:", fact)

# string1 = "Automation"
# print(string1[::-1])

# rev = ""
# for char in string1:
#     rev = char + rev

# print(rev)

# word = "madam"

# if word == word[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# name = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0
# for char in name:
#     if char in vowels:
#         count += 1

# print("Total vowels:", count)

num = int(input("Enter table number: "))

for i in range(1, 101):
    print(f"{num} x {i} = {num*i}")

"""    
===========================================================
Interview Questions

Be ready to answer:

What is Python?
Why is Python used in automation?
What are mutable and immutable objects?
Difference between == and is
Difference between list and tuple
What is indentation?
What is PEP 8?
What are Python keywords?
What are identifiers?
Explain dynamic typing
===================================================================================
"""