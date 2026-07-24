'''Number and Strings'''
num1=101
num2=102
print("The sum of {0} and {1} is {2}".format(num1,num2,num1+num2))
print(type(num1))
print(type(num2))
# find the maximum number of three numbers
print("The maximum number of {0}, {1} and {2} is {3}".format(num1,num2,103,max(num1,num2,103)))
print(max(10,20,30))
print(min(10,20,30))
print(len("hello world"))
print(sum([10,20,30]))

'''
String are immutable in python. Once a string is created, it cannot be changed.
Creating string varaible are 
s="hello"
s='world'
s=str('hi')
s=str('welcome')

Creating the empty string varaible are 
str=""
name=str()
name =''

Different between mutable and immutable data types in python are 
Mutable data types are those data types whose value can be changed after they are created. 
Examples of mutable data types are list, set, dictionary, etc.
Immutable data types are those data types whose value cannot be changed after they are created.
Example of immutable data types are int, float, string, tuple, etc.
strings are + or * with string and examples are
'''
s1="hello"  
s2="world"
s3=s1+s2
print(s3)       #helloworld
s4=s1*3
print(s4)       #hellohellohello

#Converting the string to upper case, lower case, capitalize, swapcase and replace the string
str = "Hello python"
print(str.upper())      #HELLO PYTHON
print(str.lower())      #hello python
print(str.capitalize()) #Hello python
print(str.swapcase())   #hELLO PYTHON
print(str.replace("H", "J"))  #Jello python
print(str.title())      #Hello Python

#Slicing the string
print(str[::-1])        #nohtyp olleH   
print(str[1:6])         #ello
print(str[1:6:2])       #el
print(str[1:6:-1])      #Hello Pytho
print(str[:-1])         #Hello python

#Finding the length of the string
str1 = "Hello python"
print(len(str1))        #12

#Count the occurence of the string
print(str1.count("o"))      #2

# in and not in operator are used to check the presence of a substring in a string.
str2 = "Hello python"
print("Hello" in str2)      #True
print("World" not in str2)  #False

#String Comparision
print("tim"=="tie")         #True
print("free"!="freedom")    #False
print("arrow">"aron")       #True
print("right">="left")      #False
print("right"<"left")       #False
print("right"<="left")      #False
print("abc"> " ")           #True

#Searching the string with find, count, endswith, startswith, index and rindex
string1 ="welcome to python programming"
print(string1.find("python"))        #11    
print(string1.count("o"))             #4
print(string1.endswith("programming")) #True
print(string1.startswith("welcome"))   #True
print(string1.index("to"))           #8
print(string1.rindex("o"))          #20

#isalpha(), isdigit(), isspace(), islower(), isupper() are used to check the string properties.
str3 = "Hello"
print(str3.isalpha())      #True
str4 = "12345"
print(str4.isdigit())      #True
str5 = "   "
print(str5.isspace())      #True
str6 = "hello"
print(str6.islower())      #True
str7 = "HELLO"
print(str7.isupper())      #True

#Write the reverse the string?
str8 = "Autmation"
print(str8[::-1])        #noitamtuA 
print(''.join(reversed("Automation")))      #noitamtuA

#using the split() method to split the string into a list of words.
str9 = "Hello python programming"
print(str9.split())       #['Hello', 'python', 'programming']

#using without slicing 
rev=" "
for char in str9:
    rev = char + rev
print(rev)              #gnimmargorp nohtyp olleH
