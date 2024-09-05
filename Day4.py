#------------------------functions-----------------------

"""smaller reusable chunks to organize our code
first we define functions then we call it
Simple function to greet"""
def greetings():
    print("Goog Morning")
greetings()


"""Passing information to a function (Parameters)"""
def greetings(name):
    print("Goog Morning" , name)
greetings("User ")
greetings("JOHN ")

"""in order to rename the variable
Click on the variable and press shift + F6 . Type the name and press Enter
Multiple parameters"""

def greetings(first_name , last_name):
    print(f'Good Morning {first_name}  {last_name} !')

greetings("John" , "smith") # calling function with keyword argument it will increase the readability of code.

#Exercise------create a function that calculate square of the number
num = int(input("Enter number to calculate square: "))
def square_of_num(num):
    print(f'square of {num} is {num * num}')

square_of_num(num)

#exercise-----emojis converter program into functions

def emojis_converter(msg):
    words = msg.split(" ")
    emojis = {
        ":)": "😂",
        ":(": "😔",
        "heart": "❤️",
        "lovely": "😍",
        ";) ": "😉"
    }
    output = ""
    for word in words:
        output = output + emojis.get(word, word) + " "
    return output


msg = input("> ")
result = emojis_converter(msg)
print(result)

#-------------------Exception-----------------
"""To handle the errors we use try and except concept
exit code 0 means program successfully executed wile 1 means program crashed
# example
By executing this code we encounter Value error if we put any string instead of integer value
age = int(input('Age: '))
print(age)
we can overcome this by telling python that execute this two line of try and if encounter any valueerror than instead of crashing the program print the lines present in except blog
"""
try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value Entered')

#we can add multiple type of exception cases for multiple types of errors
try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age  #but what if user enter 0 in age
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print('Invalid value Entered')







