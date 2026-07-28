'''
Function is a block of code that performs a specific task.
benefits of using function: Increase code readability and reusability.

Basic Concepts:
- Create Function
-Call function
- Parameter
- Argument

Types of Function:
Below are the two types of function in python:
1. Built-in library function:
    These are standard functions in python that are available to use.
    example: print(), input(), type(), sum(), max(), min() etc.,
2. User-defined function:
    We can create our function based on the requirements.
    example: create your own function

Syntax:
def my_function(param):
    instruction-1
    instructon-2
return result
'''
# Function without parameters
# example1:
# create or define function
def greetings():
    print("Welcome to python tutorial")
#use or call this function
greetings()         #output: Welcome to python tutorial

#function with Parameters
# Example1:-
#function to adds two numbers and print result
def add(a,b):
    return a+b
print(add(10,20))
print(add(200,300))

# def sub(a,b):
#     return a-b
# print(sub(20,10))

# def mul(a,b):
#     return a*b
# print(mul(10,5))

# def div(a,b):
#     return a//b
# print(div(10,5))

# def mod(a,b):
#     return a%b
# print(mod(10,5))

# def fibo(n):
#     a,b=0,1
#     while a<n:
#         print(a, end=" ")
#         a,b=b,a+b
#     print()

# fibo(1000)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 

'''
Return Statement: return statement is used in a function to send a result back to the place 
where the function was called. When return is executed, the function stops
runnig and immediately returns the specified value.
'''
def sub(a,b):
    return a-b
print(sub(20,10))

'''
Function with a return value

'''