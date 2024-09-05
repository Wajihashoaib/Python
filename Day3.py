#-----------------------for loops--------------------
"""
In python for loops are use to iterate over items of a collection
Difference between for and while?
while
-----
The while loop is used when you want to repeatedly execute a block of code as long as a specified condition remains true.
It's ideal for situations where the number of iterations is not known beforehand and depends on some condition that may change over time
-----

for
-------
The for loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or other iterable objects.
It's ideal for situations where you want to iterate over a known range of values or elements in a collection.
-------
"""
#example
#iterate over string
for item in 'Python':
    print(item)

#iterate over list
for item in [1,2,3,4,'name',8]:
    print(item)

#for creating rang of numbers using loop we have range function
for item in range(10):
    print(item)

for item in range(5,10): #starting from 5 ending at 9
    print(item)

for item in range(1,10,3): #1-10 with 3 steps forward
    print(item)

#printing index number along with item
#solution 1 using enumerate function
for index, item in enumerate([1,2,3,4,'name',8]) :
    print(f'Index: {index} Item: {item}')

#soltui0n 2 using manual counter
index = 0
for item in range(10):
    print('index: ',index, ' item: ', item)
    index +=1

"""
Exercise, find out total cost of all the items in list of prices
"""

#soltuion 1
price_list = [200, 300,500, 600]
total_cost = 0
for item in price_list:
    total_cost = item + total_cost
print("total cost is: ", total_cost  )

#Exercise-----Print F shape using for loop
numbers = [5,2,5,2,2]
for i in numbers:
    print("X" * i)

#let's print E using python for loop
numbers = [5,2,5,2,5]
for i in numbers:
    print("X" * i)

#---------------------Nested for loops-------------------
"""
print output
(x, y)
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
"""
print("(x , y)")
for x in range(2):
    for y in range(3):
        print(x ," ", y)

#-------------------Lists in Python---------------------
names = ['apple' , 'banana', 'orange' , 'cherry', 'berry']
print(names[0])
names[4] = 'blue berry'
for item in names:
    print(item)
names.append('jam')
for item in names:
    print(item)
names.pop()
for item in names:
    print(item)
names.sort()
for item in names:
    print(item)
new_names= names.copy()
for item in new_names:
    print(item)


#Exercise----WAP to find the largest number in list
#solution 1
list = [3,5,6,7,83,8,9,10]
list.sort()
print(list[-1])

#soltuion 2 using algorithm
my_list = [3,5,6,7,83,8,9,10]
max = my_list[0]
for item in my_list:
    if item > max:
        max = item
print(max)

#--------------2d list----------------
matrix = [
    [1,2,3],
    [2,4,5],
    [6,7,8]
]

print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])
print(matrix[1][1])
matrix[1][1] = 3
print(matrix[1][1])

# Define a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the matrix
for row in matrix:
    for item in row:
        print(item, end=" ")  # Print each item followed by a space
    print()  # New line after each row

#Exercise---WAP to remove duplicate in a list
my_list = [1,2,2,3,4,5,6,7,2]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)


#-----------------------Tuples-------------------------
#tuples are nothing but immutable list we cannot modify them
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

languages = ('Python', 'Swift', 'C++')
# access the first item
print(languages[0])
#cordinates of tuppple
x = languages[0]
y = languages[1]
z = languages[2]
#we can use it like this also
x , y , z = languages
print(x , y, z)

fruits = ('apple','banana','orange')

# iterate through the tuple
for fruit in fruits:
    print(fruit)
#Check if an Item Exists in the Tuple
colors = ('red', 'orange', 'blue')
print('yellow' in colors)    # False
print('red' in colors)       # True

#----------------------Dictionaries in Python----------------
#Nothing but a key value pair----Key should be unique---and it can be case sensitive
#example
#Name: John Smith
#Phone: 23387648
#email: John@gmail.com
#Keys:  Values
customers = {
    "name" : "John Smith",
    "age": 36,
    "is_verified": True
}
print(customers.keys()) #printing keys
print(customers.values()) #printing values
print(customers['name']) #printing 1st value
#printing all keys using loop
for item in customers:
    print(item)

#printing all values using loop
for item in customers:
    print(customers[item])

#print(customers['Name']) #gives an error because of capital N
#There we use get method if not found the given key written something else without giving key error
print(customers.get('Name', 'Key not found because of Capital N'))

#dictionaries are mutable, means we can change them
customers['name'] = 'Jack Smith'
print(customers['name'])

#we can also add the key in dictionaries
customers['Birthdate'] = 'Jan 1 1998'

print(customers.values())

#Exercise--------Convert dial numbers into words

phone_number = input("Phone: ")
my_dict = {
    '1' : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}
# output = ""
# for digit in phone_number:
#     output = output + my_dict[digit] + " "
# print(output)

#but what if user input any other number except 1234?
output = ""
for digit in phone_number:
    output = output + my_dict.get(digit, "!") + " "
print(output)

#it will return ! mark if user input anything else than specified digit


#----------------------Emoji Convertor------------------------
msg = input("> ")
words = msg.split(" ")
emojis = {
    ":)" : "😂",
    ":(" : "😔",
    "heart" : "❤️",
    "lovely" : "😍",
    ";) " : "😉"
}
output = ""
for word in words:
    output = output + emojis[word] + " "
print(output)
