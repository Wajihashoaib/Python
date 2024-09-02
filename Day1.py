#Python Practice Programs

#print hello world
print("Hello World, I am learning Python")

#print any string
print("o-------------------o")

#print using multiplication
print("* " * 10) #horizntal

print("* \n" * 10) #vertical


#learning about variables
"""Variable is containers that store values.
Python is dynamically typed means We do not need to
declare variables before using them or declare their type."""

price = 10  #price is box containing value 10 (int)
rating = 4.0 #float point variable
name = 'wajiya' #string variable
is_published = False #bool keyword, keywords are the reserve words
print(price, rating , name , is_published)


"""
Exercise-1
create three variables for person name age and status
to check whether the patient is old or new
"""

name = 'Wajiya'
age = 22
is_new = False

print(name , age , is_new)


''' user input'''
#take input from user using built-in function
name = input("what is your name? ") #ask from user and if we want to store the value of user input into the memory we use variable
print("hi, ", name)

"""Exercise 2
Ask a Question to person about his name and favorite color.Then print msg like 'wajiya loves white"""
name = input('What is your name mam? ')
color = input("what is your favorite color mam? ")
print(name , " likes " , color)

"""python type conversions"""
birth_year = int(input("Birth Year : ")) #input by default store values in str format so we need to type cast here using int function
age = 2024 - birth_year
print(age)

#in order to find the type of variable we need to use the function called type

print(type(age))
print(type(birth_year))

'''Exercise 3
Ask a user their weight (in pounds), convert it into kilograms and print on the terminal'''

weight_in_pounds = float(input('enter you weight in pounds: '))
weight_in_kg = int(weight_in_pounds / 2.205 )
print(weight_in_kg)
#playing with strings

python = "Python is most popular programming language"
javascript = "Javascript 's reason of popularity is web developmet "
long_string = """
This is dummy paragraph that we need to showcase only \n for how we can use long paragraph in python and print it
"""
print(python)
print(javascript)
print(long_string)
course = "Python for beginners"
#         01234567891011
print(course[0])
print(course[7])
print(course[-1]) #for last char
print(course[0:3]) #print from 0 index to 2nd index-not include 3rd index
print(course[0:])  #print complete string starting from index 0
print(course[2:])
print(course[:5])
print(course[:]) #copy and clone string

another = course[:] #example
print(another)

"""
Exercise 4
what is the output of following program
name = 'Jennifer'
print(name[1:-1])
answer is ennife
"""
name = 'Jennifer'
print(name[1:-1])
"""Formated Strings
String formatting is also known as String interpolation.
It is the process of inserting a custom string or variable in predefined text
The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}.
"""
#example:- print Wajiya [shoaib] is a coder
#code will be
first_name = 'wajiya'
last_name = 'shoaib'
message = first_name + ' [' + last_name + '] '+ 'is a coder'
print(message)

#this code is complex and in order to do task like that we have formatting option
fisrt_name = 'wajiya'
last_name = 'shoaib'
msg = f'{fisrt_name} [{last_name}] is a coder'
print(msg)

price = 59 #values
txt = f"The price is {price} dollars"
print(txt)

price = 59.978  #modifiers
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars" #opeartions
print(txt)

"""to format values in an f-string , add placeholders {}, a placeholder can contain variables,
operations, functions, and modifiers to format the value."""

#string methods in python
course = 'python for beginners'
print(len(course))
"""return the length of the string
#in order to find all the possible functions u can apply on string
#write name of the string like course and place . after the name ex:- course."""
print(course)
print(course.upper()) #convert into uppercase
print(course.lower()) #convert into lowercase
print(course.find('p')) #find the letter p
print(course.find('P'))  #finf the letter P as it is not present in the string it will give -1
print(course.find('beginners')) #return the index number from where the giving word is staring
print(course.replace('beginners' , 'absolute beginners'))
print(course)
print("Python" in course) #return false as Capital P is not present
print("python" in course) #return True

#The end for today will start from operators tomorrow In Sha Allah
x = 10 + 2 * 3 #3*2=6 + 10 = 16
print(x)
"""precedence
brackets
exponentiation 2 ** 3
multiplication or division
addition or subtraction"""
x = 10 + 2 * 3 ** 2 #3 * 3 = 9 * 2 = 18 + 10
print(x)
x = (10 + 2 )* 3 ** 2
print(x)

