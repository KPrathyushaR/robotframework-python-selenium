'''
Dictionaries are a type of data structure in Python that can hold an ordered collection of items.
indexed, changeable, and allow duplicate values. 
Dictionaries are written with curly brackets, and they have keys and values.
A dictionary is a collection which is unordered, changeable and indexed.
Dictionaries have keys and values, and you can access the items by referring to their key name.
Creating a dictionary variable:
'''
mydict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(mydict)
print(type(mydict))

mydict1 = dict()  #Empty dictionary
print(mydict1) 

mydict2 = {
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(mydict2["brand"])  # Accessing the value of a key
print(len(mydict2))  # Find the length of a dictionary

#using the get() method to access the value of a key
x = mydict2.get("model")
print(x)

#change the values in dictionary
mydict2["brand"] = "Chevrolet"  # Change the value of a key
print(mydict2)
mydict2["year"]="1997"
print(mydict2)

# for i in mydict2:
#     print(i)            #print only keys from dictionary

# for i in mydict2:
#     print(mydict2[i])  #print only vales from dictionay 

# for i in mydict2.values():
#     print(i)

for x,y in mydict2.items():
    print(x,y)

#check key is exist in dictionary or not
mydict2={"brand":"hyudai",
         "year" :8900,
         "model":"shift"
         }

if "model" in mydict2:
    print("exist")
else:
    print("not exists")

mydict2.pop("year")
print(mydict2)    #{'brand': 'hyudai', 'model': 'shift'}

del mydict2
print(mydict)



