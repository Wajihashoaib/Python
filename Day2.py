#math functions
import math as m

x , y = 4 , 4.5
print(m.sqrt(x))
print(m.pow(2,3))
print(m.factorial(x))
print(m.floor(y))
print(m.ceil(y))
print(m.pi)
print(m.floor(m.pi))

# ---------------------if-else statements-----------------

is_hot = False
is_cold = False
if is_hot:
    print("its a hot day \nDrink Plenty of water ")
elif is_cold:
    print("it's a cold day \nWear warm clothes ")
else:
    print("it's a lovely day")
print("Enjoy your day")

"""exercise
# Price of a house is $1M.
# If buyer has good credit,
#   they need to put down 10%
# Otherwise
#   they need to put down 20%"""

#Solution-1
price = 1000000
is_credit = False
if is_credit:
    print('buyer has good credit. you need to put down: ',int (10/100 * price))
else:
    print('buyer not has good credit. you need to put down: ', int(20 / 100 * price))
#Solution-2
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: {down_payment}")

#------------------------logical Operators-----------------
"""Exercise---- if applicant has high income and good credit Eligible for loan"""

has_high_income = True
has_good_credit = False
if has_high_income and has_good_credit:
    print('Eligible for loan')
else:
    print("Not eligible for loan")

#if applicant has high income or good credit Eligible for loan
has_high_income = True
has_good_credit = False
if has_high_income or has_good_credit:
    print('Eligible for loan')
else:
    print("Not eligible for loan")

#if applicant has high income and no criminal record Eligible for loan
has_high_income = True
has_criminal_record = False
if has_high_income and not has_criminal_record:
    print('Eligible for loan')
else:
    print("Not eligible for loan")


#-----------------Relational Operators-------------------
"""if temperature is greater than 30
  it's a hot day
otherwise
  if it's less than 10 it's a cold day
otherwise
  it's neither hot nor cold"""

temp = int(input("What is the temperature today? "))
if temp > 30:
    print("it's a hot day")
elif temp < 10:
    print("it's a cold day")
else:
    print("it's neither hot nor cold")


"""Exercise
if name is less than 3 characters long
    name must be at least 3 characters
otherwise
    if it's more than 50 characters long name can be a maximum of 50 characters
otherwise
    name looks good"""

#Solution

name = input("What is your name? : ")
length_of_name = len(name)
if length_of_name < 3:
    print("Name must be at least 3 characters")
elif length_of_name > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good! ")


"""Exercise----Create weight converter Program"""

# Sample output
# Weight: 160
# (L)bs or (K)g: l
# You are 72.0 kilos

weight = float(input("Enter your weight: "))
choice = input(f'(L)bs or (K)g: '  )
if choice == 'L' or choice == 'l':
    print(f'your weight is: {weight * 0.45} Kilos')
elif choice == 'K' or choice == 'k':
    print(f'your weight is: {round(weight / 0.45) } pounds')
else:
    print("Please enter correct choice")

#Solution-2

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

#---------------while loop in python-------------------
"""while loop runs the code as long as the condition is true"""

i = 1
while i <= 5:
    print(i)
    i = i + 1
print('Done')
#print the table of 2
i = 1
while i <= 10:
    print(f' 2 * {i} = {2*i}')
    i = i + 1
print('Done')
#let's print patterns using while loop
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print('Done')


"""Exercise---Create basic guessing game program using file"""

number = 9
attempts = 1
guess_limit = 3
while attempts <= guess_limit:
      guess = int(input("Guess : "))
      attempts = attempts + 1
      if guess == number:
          print("you win")
          break
else:
     print("sorry")

"""Exercise-----Create Basic Car game program"""

press = ''
while press != 'quit':
    press = input("> ")
    if press == 'help':
        print("start - to start the car\nstop - to stop the car\nquit - to exit")
    elif press == 'start':
        print("Car Started")
    elif press == 'stop':
        print("Car stopped")
    elif press == "quit":
        break
    else:
        print("Sorry, I don't understand it. ")

#solution-2

while True:
    press = input("> ")
    if press == 'help':
        print("start - to start the car\nstop - to stop the car\nquit - to exit")
    elif press == 'start':
        print("Car Started")
    elif press == 'stop':
        print("Car stopped")
    elif press == "quit":
        break
    else:
        print("Sorry, I don't understand it. ")
#fixing some bugs like what if car is already started or already stoped?
started = False
while True:
    press = input("> ")
    if press.lower() == 'help':
        print("start - to start the car\nstop - to stop the car\nquit - to exit")
    elif press.lower() == 'start':
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car Started")
    elif press.lower() == 'stop':
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped")
    elif press.lower() == "quit":
        break
    else:
        print("Sorry, I don't understand it. ")
#now this program is bug free also it is not case-sensitive