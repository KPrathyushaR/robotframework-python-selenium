#===========================================================
'''
Topics are 
print()
range()
input()

'''

#write the first code in python ?
print("Hello world")

#using the range of the odd number, even number and descending order
print(list(range(10)))
print(list(range(0,10)))
print(list(range(1,10,2))) #odd number
print(list(range(2,10,2))) #even number
print(list(range(10,0,-1))) #descending order
print(list(range(-10,-5)))

#how to take the input from users
# print(input())
# print(int(input()))
# print(float(input()))

#write the keywords in python ?
import keyword
print(keyword.kwlist)
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

''' Variables
what are variables?
- variables are to store the data which contains the values.
example of 
x=100
y="name"

- Dynamically typed programming languge.'''

#Write the simple programming to swapping two variables?
x=10
y=20
print("Before Swapping x,y:", x,y)
x,y=y,x
print("After Swapping x,y:", x,y)

#how to delete the varible?
a=10
b=20
print("Before deleting the a:",a)
del a
# print("After deleting the a",a) #output is ais not defined.

'''
Operators:
-operators are symbol which will perform an operation between 2 oe more varibles.
-Arthimetic operand
-Assignment operand
-Comparsion operand
- Identify operand
-Bitwise operand
'''

#Concentation is it will perform the addtion and it will concentated the two string.
print(10+10)
print(10.3+10.9)
print("hello"+"guru")
# print(10+"guru")  #TypeError because unsupported operand type of int and string
print(True+True)
print(True+3)

#Formatiing Output
name="prathyusha"
age=27
salary=20000

print("my name is {}, my age is {}, my salary is {}".format(name, age, salary))
print("my name is %s, my age is %d, my salary is %d"%(name,age, salary))

#f-string
print(f"my name is {name}, my ageis {age}, my salary is {salary}")

'''
Condition  Statements
===================================================================
1. Conditional Statements - if-else, if-elif-else
2. Looping Statements - While, for loops
3. Jumping Statements - Break, Continue
'''

#Find a number is even or odd number
num=27
if num%2==0:
    print(f"Even number: {num}")
else:
    print(f"Odd number: {num}")

#ex2:
num=10
if num>0:
    print("Postive Number")
elif num==0:
    print("zero")
else:
    print("Negative Number")

#ex3:if else in single line(ternary number)
num=10
print("even number") if num%2==0 else print("odd number")

#ex4:if else in muliple statement in single line
a=10
{print("hello"), print("python")} if a>=10 else {print("hi"), print("java")}

'''
Looping Statements: While and For Loop
Using the While Loop, we need these intilization, condition and incrementation
'''
i=1
while i<=10:
    print(i, end=" ")
    i+=1
print("Done!!!!!")

a=10
while a>=1:
    print(a, end=" ")
    a-=1
print("Reversed done!!!")

#Example of Fiboccai series:
def fibo(n):
    a,b=0,1
    while a<n:
        print(a, end=" ")
        a,b=b,a+b
    print()
fibo(1000)

#======================================================
#For Loop
for i in range(10):
    print(i)

for i in range(1,10, 2):
    print(i)

for i in range(10,1,-1):
    print(i)
#=========================================================
#Jumping Statements  are break and continue

# break will stop the iteration
for i in range(10):
    if i==3:
        break 
    print(i)

#continue will continue the iteration
for i in range(1,10):
    if i==5:
        continue
    print(i)

# example :write the python programming for thr weeks and months?
# write the python progrmming for the table 5?

# week=input('Enter the days: ')
week="Friday"
if week == 'Sunday':
    print("Sunday is fun day")
elif week == 'Monday':
    print("Monday is Working Day")
elif week == 'Tuesday':
    print("Tuesday is Festival Day")
elif week == 'Wednesday':
    print("Wednesday is Offer Day")
elif week == 'Thursday':
    print("Devotional Day")
elif week == 'Friday':
    print("Chill Day")
elif week == 'saturday':
    print("Weekend Day and Party time")
else:
    print("Spelling Mistake and First Letter is Capital")

#===============================================================
num=5
for i in range(1,11):
    print(f"Display the num: {num} x {i} = {num*i}")

'''
Output:-

Display the num: 5 x 1 = 5
Display the num: 5 x 2 = 10
Display the num: 5 x 3 = 15
Display the num: 5 x 4 = 20
Display the num: 5 x 5 = 25
Display the num: 5 x 6 = 30
Display the num: 5 x 7 = 35
Display the num: 5 x 8 = 40
Display the num: 5 x 9 = 45
Display the num: 5 x 10 = 50
'''


