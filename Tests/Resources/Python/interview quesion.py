list1 = [1,2,3,4]
print(list1.pop())
print(list1.remove(1))
print(list1)

'''
pop() removes an element by index (default: last element) and returns the removed element.
remove() removes an element by value and returns None. It raises a ValueError if the value is not found.
Final Output:-
----------------
4
None
[2, 3]
'''

def foo(i, x=[]):
  x.append(x.append(i))
  return x
for i in range(3):
   y = foo(i)
print(y)   #output:[0, None, 1, None, 2, None]

import re
m = re.search(r'\d+', 'hi234yes')
print(m.group())  #output:234

# Write Python programs for:
# 1. Print all even numbers from 1 to 100

for i in range(1, 101, 2):
   if i%2 ==0:
      print("Even number")
   else:
      print("Odd number")

# Find the largest number in a list
number=[10,20,90]
largest=number[0]
for i in number:
   if i > largest:
      largest = i
print(largest)

# Count uppercase and lowercase characters
text = input("Enter a string: ")

upper = 0
lower = 0

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)

#write the vowels in string
word=input("Enter the character:")
vowels="aeiouAEIOU"
count=0
for char in word:
   if char in vowels:
      count+=1
print("Total the Vowels:", count)

# Reverse a string without slicing
word="Automation"
rev=""
for char in word:
    rev= char +rev
print(rev)

# Find duplicate elements in a list
numbers = [10, 20, 30, 20, 40, 10, 50]
duplicates = []

for i in numbers:
    if numbers.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate elements:", duplicates)