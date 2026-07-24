'''
A Set is a collection of unique elements.
A set is a collection which is unordered, unchangeable*, and unindexed.
in python sets are written by {}.
remove duplicates from a list using set() function.
Creating a set variable:                
'''
set1={1,2,3,4,5,6,7,8,9}
print(set1)

#accessing set items
for i in set1: 
    print(i)

#value existence in set
if 5 in set1:   
    print("Yes, 5 is in the set")

#adding items to a set
set1.add(10)  #add() method
print(set1)
set1.update([11,12,13])  #update() method
print(set1)

#find the length of a set
print(len(set1))

#removing items from a set
set1.remove(13)  #remove() method  
print(set1)
# set1.remove(17)        #remove() method
# print(set1)            #will raise an error if the item is not found.
set1.discard(12)         #discard() method
print(set1)
set1.discard(17)      #discard() method
print(set1)            #will not raise an error if the item is not found.

#clearing a set
set1.clear()  #clear() method
print(set1)   #set() will be printed

# del set1  #delete the set completely
# print(set1)  #will raise an error because the set no longer exists

# want to join the two sets? use union() method or | operator
set2={1,2,3,4,5}
set3={6,7,8,9,10}
set4=set2.union(set3)  #union() method
print(set4)

set5=set2|set3  # | operator
print(set5)

set6={1,2,3,4,5}
set7={4,5,6,7,8}
set8=set6.update(set7)  #update() method
print(set6)  #set6 will be updated with set7 values