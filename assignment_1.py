#session_1
"""
Exercise 1: Basic Variable Assignment
Exercise 2: Type Conversion
Exercise 3: String Formatting
Exercise 4: Control Structures
Exercise 5: Arithmetic Operations
Exercise 6: Comparison and Logical Operators
Exercise 7: Ternary Conditional Expression
"""


#Task 1: Assign values to variables of different data types (integer, float, string, boolean) and print them..
"""
var1, var2, var3, var4 = 12, 3.4, 'ashish', True
print(var1, var2, var3, var4)
"""

#Task 2: Write a script that takes a user input (string), converts it to an integer, performs a calculation, 
#and then prints the result.
"""
var1 = 23
#var1 = input("\nËnter a num: ")
print("Before covert: ", var1, type(var1))
var1 = int(var1)
print("Äfter convert: ", var1, type(var1))
"""

#Task 3: Create a string using both f-strings and the format() method that includes a variable integer and float, 
#displaying them to two decimal places.
"""
name = 'Bhumi'
id = 12
age = 25.5
print('\n', f"My name is {name}, my id is {id}", "and I am {:.2f}yr old.".format(age))
"""

#Task 4: Write a script that asks the user for a number and checks if the number is positive, negative, or zero, 
#printing an appropriate message for each case.
"""
def numCheck(num):
    if (num>0):
        print("Number is possitive")
    elif (num<0):
        print("Number is negetive")
    else:
        print("Number is zero")

number = int(input("\nÉnter a number: "))
numCheck(number)
"""

#Task 5: Write a script that performs and prints the results of addition, subtraction, multiplication, division, 
#and exponentiation of two numbers provided by the user.
'''
def calculate(num1, num2):
    print("addition of given num is: ", num1+num2)
    print("substraction of given num is: ", num1-num2)
    print("multiplication of given num is: ", num1*num2)
    print("division of given num is: ", num1/num2)
    print("exponential of given num is: ", num1**num2)

number1 = int(input("\nÉnter 1st number: "))
number2 = int(input("Énter 2nd number: "))
calculate(number1, number2)
'''

#Task 6: Create a script that asks the user for their age and determines if they are a child, teenager, adult, 
#or senior, using both comparison and logical operators.
"""
def ageCheck(num):
    if ((num>0) and (num<12)):
        print("you are child")
    elif ((num>=12) and (num<20)):
        print("you are teenager")
    elif ((num>=20) and (num<60)):
        print("you are adult")    
    else:
        print("you are senior")

number = int(input("\nÉnter your age: "))
ageCheck(number)
"""

#Task 7: Write a script that determines whether a user's input number is even or odd using a ternary conditional expression.
"""
number = int(input("\nÉnter a number: "))
res = "Even" if (number%2)==0 else "Ödd"
print('ýour number is: {}'.format(res))
"""

#nested ternary operatore
"""
number = int(input("\nÉnter a number: "))
res = ">50" if (number>50) else "20-50" if (number>20) else '<20'
print('ýour number is: {}'.format(res))
"""

#=======================================================================================================================

#Session 2:
"""
Exercise 1: List Manipulation
Exercise 2: 2D Array Access
Exercise 3: Dictionary Operations
Exercise 4: Set Operations
Exercise 5: For Loop Practice
Exercise 6: While Loop Practice
Exercise 7: Combined Data Types
"""


#Task 1: Create a list of your favorite movies. Add two more movies, remove one, and print the updated list.
'''
list1 = ["Ham sath sath hai", "Ham aapke hai koun", "Bagban"]
print(list1)
list1.append('Bahubali')
list1.append('Kalki')
print(list1)
list1.remove('Bagban')
print(list1)
'''
#Task 2: Create a 3x3 matrix and print each element using nested loops.
'''
list2 = [3]
list2 = ['á', 3, 5]
print(list2)

list3 = ['ásh', 'kir', 'shwe'], ['kar', 'shar', 'vhru'], ['balu', 'shri', 'ándu']
print(list3)
print(list3[0][0])
print(list3[0][1])
print(list3[0][2])
print(list3[1][0])
print(list3[1][1])
print(list3[1][2])
print(list3[2][0])
print(list3[2][1])
print(list3[2][2])
'''

#Task 3: Create a dictionary with information about a book (title, author, year). Add a key for genre, update the year, 
#and print all the keys and values.
'''
dict1 = {'title':'Supremology', 'áuthor':'ramana', 'year':2016}
print(dict1)
dict1['work in'] = 'Software industry'
print(dict1)
dict1['year'] = 2024
print(dict1)
'''

#Task 4: Create a set of unique words from a given sentence.

sentence = '''When you consider the powerful influences over your financial life—if you’ve ever done that before 
now—maybe you tick off the books you read, television shows you watched, college you attended, neighborhood you 
grew up in. Those are all real and potentially made an impact on you. But the most powerful force in your financial 
life to this day is quite possibly something you’ve never really considered.'''
'''
set1 = ()
words = sentence.split()
print(words)
unc_words = []

for i in words:
    if(i[0]=='w' or i[0]=='W'):
        unc_words.append(i)

unc_words = set(unc_words)
print(unc_words, "and type is: ", type(unc_words))
'''

#Task 5: Write a for loop to print the first 10 numbers in the Fibonacci sequence.
'''
def Fibonacci(num):
    feb = []
    for i in range(num):
        if i<2:
            feb.append(i)
            print(i, end=' -> ')
        else:
            feb.append((feb[i-1])+(feb[i-2]))
            print((feb[i-1])+(feb[i-2]), end=' -> ')
            
    print('\n List is: ', feb)

Fibonacci(10)
'''

#Task 6: Write a while loop to reverse a string.
'''
def reverse(str1):
    length = len(str1)
    str2 = ''
    
    while(length):
        str2 = str2 + str1[length-1]
        length-=1
        
    print('original string: ', str1)
    print('reverse string: ', str2)    
        
reverse("AUTOSAR")
'''

#Task 7: Create a list of dictionaries, where each dictionary represents a student with keys for name and grade. 
#Print each student's name and grade using a loop.

dict1 = {'stu1':{'name':'vrishali', 'grade':'8.7'}, 
         'stu2':{'name':'nishali', 'grade':'7.9'}, 
         'stu3':{'name':'sweta', 'grade':'9.0'}}

for i in dict1:
    print(dict1[i])
    
print(end="\n")

for stu in dict1.values():
    print('stu => ', stu)
    
    for i in stu.keys():                            #print keys only
        print(i)    
        
    for i in stu.values():                          #print values only
        print(i)      
    
    for k, l in stu.keys(), stu.values():           # wrong output  1st print keys then values
        print(k,": ", l, end="\n")
        
    for i, j in stu.items():                        # i=key and j=values -results as expected
        print(i,": ", j, end="\n")    
    print(end="\n")