"""
Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum."""
def cal(num1, num2):
    product = num1 * num2
    sum = num1 + num2
    if product <= 1000:
        return product
    else:
        return sum


print(cal(20,30))
print(cal(40,30))
"""
Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number
"""
print("Printing current and previous number sum in a range(10)")
previous_no = 0
for current_no in range(0,10):
    sum = previous_no + current_no
    print(f'Current Number {current_no} Previous Number  {previous_no}  Sum:  {sum}')
    previous_no = current_no


"""
Write a Python code to accept a string from the user and display characters present at an even index number.
"""
str = input("Original String is: ")
print("Printing only even index chars \n")
for i in range(0 , len(str)-1 , 2):
    print(str[i])


"""
Write a Python code to remove characters from a string from 0 to n and return a new string
"""
# method 1
def remove_chars(string, n):
    for i in range(n, len(string)):
        print(string[i])


remove_chars("Wajiya" , 2)

# method 2
def remove_chars(string, n):
    print("Original String: " , string)
    new_string = string[n: ]
    return  new_string


print("New String: ",remove_chars("Wajiya" , 2))
"""
Check if the first and last numbers of a list are the same
return True if the list’s first and last numbers are the same. If the numbers are different, return False.
"""
def check_ist_last(given_list):
    start_index = given_list[0]
    last_index = given_list[-1]
    if start_index == last_index:
        print("True")
    else:
        print("false")

list =  [75, 65, 35, 75, 30]
check_ist_last(list)

list = [10, 20, 30, 40, 10]
check_ist_last(list)

"""
Write a Python code to display numbers from a list divisible by 5
"""
number = int(input("Enter any number: "))
if number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")
