'''
Collections are four type od data: 
List
Set
Tuple
Dictionary
==============================================================
Lists are a type of data structure in Python that can hold an ordered collection of items.
In python lists are written by {}.
A list is a collection which is ordered and changeable.
They are mutable, meaning that their contents can be changed after they are created. 
Lists can contain elements of different data types, including other lists.
Creating a list variable:

'''
num=[1,2,3]
print(num)
print(type(num))
mylist=list()  #Empty list
print(mylist)

#how to accessing fromthe list

mylist=["apple", "kiwi", "orange","banana"]
print(mylist[1])
print(mylist[3])
print(mylist[-1])
mylist[0]="potato"
print(mylist)

#Example: Range of the index
mylist1=["apple", "kiwi", "orange","banana","carrot", "potato"]
print(mylist1)
print(mylist1[1:5])
print(mylist1[-4:-1])

#Change item values
mylist1[2]="tomato"  #this will change the values based on index
print(mylist1)

#read the list items using loop
for fruits in mylist1:
    print(fruits)

#check if item is exist in the list or not
mylist=["apple", "bananana", "cherry"]
if "apple" in mylist:
    print("yes, apple is present")
else:
    print("no, apple is not present")

#list length (counting number of items in the lit)
print(len(mylist1))

#Add new items in the list 
#append() and insert()
#append() - adding new item at the end of the list.
#insert() - inserting the new i
mylist1.append("avocando")
print(mylist1)          #['apple', 'kiwi', 'tomato', 'banana', 'carrot', 'potato', 'avocando']

mylist1.insert(2,"grapes")
print(mylist1)          #['apple', 'kiwi', 'grapes', 'tomato', 'banana', 'carrot', 'potato', 'avocando']   

#removng the items from the list
#remove() - removing the item based on the value.
#pop() - removing the item based on the index.
mylist1.remove("grapes") 
print(mylist1)          #['apple', 'kiwi', 'tomato', 'banana', 'carrot', 'potato', 'avocando']
mylist1.pop(2)
print(mylist1)          #['apple', 'kiwi', 'banana', 'carrot', 'potato', 'avocando']

del mylist1[1]
print(mylist1)          #['apple', 'banana', 'carrot', 'potato', 'avocando']    

#clear() - removing all the items from the list.
mylist1.clear()
print(mylist1)          #[]

#copying the list
mylist1=["apple", "kiwi", "tomato", "banana", "carrot", "potato", "avocando"]
#copy() - copying the list to another list. 
mylist2 = mylist1.copy()
print(mylist2)          #['apple', 'kiwi', 'tomato', 'banana', 'carrot', 'potato', 'avocando']

#list()- converting the other data types to list.
mylist3 = list(("apple", "kiwi", "tomato", "banana", "carrot", "potato", "avocando"))
print(mylist3)          #['apple', 'kiwi', 'tomato', 'banana', 'carrot', 'potato', 'avocando']

#approach 1: Common items in the list using set intersection
lis1=[1,2,3,4,5]
list2=[2,3,4,1,7]
common_items = list(set(lis1) & set(list2))
print(common_items)         #[1,2,3,4]

#using the looing to find the common items in the list
lis1=[1,2,3,4,5]
list2=[2,3,4,1,7]
common_items = []
for item in lis1:
    if item in list2:
        common_items.append(item)
print(common_items)         #[1, 2, 3, 4]

#compare the two lists
lis1=[1,2,3,4,5]
list2=[1,2,3,4,5]
if lis1==list2:
    print("Both lists are equal")
else:
    print("Both lists are not equal")
