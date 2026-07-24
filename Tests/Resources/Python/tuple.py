'''
Tuples are a type of data structure in Python that can hold an ordered collection of items.
In python tuples are written by ().
A tuple is a collection which is ordered and unchangeable.
They are immutable, meaning that their contents cannot be changed after they are created.
Tuples can contain elements of different data types, including other tuples.
Creating a tuple variable:
'''
num=(1,2,3)
print(num)
print(type(num))
mytuple=tuple()  #Empty tuple
print(mytuple)

#how to accessing from the tuple

mytuple=("apple", "kiwi", "orange","banana")
print(mytuple[1])
print(mytuple[3])
print(mytuple[-1])
#mytuple[0]="potato"  #This will raise an error because tuples are immutable
#print(mytuple)

#Example: Range of the index
mytuple1=("apple", "kiwi", "orange","banana","carrot", "potato")
print(mytuple1)
print(mytuple1[1:5])
print(mytuple1[-4:-1])

#Change item values
#Note: Tuples are immutable, so you cannot change their values directly.
#However, you can convert them to lists, modify the list, and then convert back to a tuple.

#read the tuple items using loop
for fruits in mytuple1:
    print(fruits)

#check if item is exist in the tuple or not
mytuple=("apple", "bananana", "cherry")
if "apple" in mytuple:
    print("yes, apple is present")
else:
    print("no, apple is not present")

#tuple length (counting number of items in the tuple)
print(len(mytuple1))

#Add new items in the tuple 
#Note: Tuples are immutable, so you cannot add new items directly.
#However, you can concatenate tuples to create a new tuple.

new_tuple = mytuple1 + ("avocando",)
print(new_tuple)          #('apple', 'kiwi', 'orange', 'banana', 'carrot', 'potato', 'avocando')

#removng the items from the tuple
#Note: Tuples are immutable, so you cannot remove items directly.
#However, you can concatenate tuples to create a new tuple without the desired item.

new_tuple = mytuple1[:-1]  # Remove the last item
print(new_tuple)          #('apple', 'kiwi', 'orange', 'banana', 'carrot', 'potato')

#del statement - deleting the entire tuple
del mytuple1
#print(mytuple1)          #This will raise an error because the tuple is deleted

#list()- converting the other data types to list.
mylist3 = list(("apple", "kiwi", "orange", "banana", "carrot", "potato"))
print(mylist3)          #['apple', 'kiwi', 'orange', 'banana', 'carrot', 'potato']

#copy the tuple to another tuple
mytuple1=("apple", "kiwi", "orange","banana","carrot", "potato")
mytuple2 = mytuple1  # This creates a reference to the same tuple
print(mytuple2)          #('apple', 'kiwi', 'orange', 'banana', 'carrot', 'potato') 

#jointhe tuple 
mytuple1=("apple", "kiwi", "orange","banana","carrot", "potato")
mytuple2=("grapes", "mango", "papaya")
mytuple3 = mytuple1 + mytuple2
print(mytuple3)          #('apple', 'kiwi', 'orange', 'banana', 'carrot', 'potato', 'grapes', 'mango', 'papaya')

#approach 1: Common items in the tuple using set intersection
tup1=(1,2,3,4,5)
tup2=(2,3,4,1,7)
common_items = list(set(tup1) & set(tup2))
print(common_items)         #[1,2,3,4]
con=tuple(common_items)
print(con)                  #(1, 2, 3, 4)

#approach2: Common items in the tuple using looping
tup1=(1,2,3,4,5)
tup2=(2,3,4,1,7)
common_items = []
for item in tup1:
    if item in tup2:
        common_items.append(item)
print(common_items)         #[1, 2, 3, 4]
con=tuple(common_items)
print(con)                  #(1, 2, 3, 4)  

#compare the two tuples
tup1=(1,2,3,4,5)
tup2=(1,2,3,4,5)
if tup1==tup2:
    print("Both tuples are equal")
else:
    print("Both tuples are not equal")