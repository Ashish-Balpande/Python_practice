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
#OR
'''
set1 = ()
words = sentence.split()
print(words)
unc_words = []
work

word1 = unc_words[0]

for i in words:
    if word1 is not:
        word1.append(i)

unc_words = set(unc_words)
print(unc_words, "and type is: ", type(unc_words))
print(word1)
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
'''
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
'''
    
#=======================================================================================================================

#Session 3:
'''
Exercise 1: Basic Function Creation
Exercise 2: Scope and Lifetime
Exercise 3: Using Standard Modules
Exercise 4: Creating and Importing Custom Modules
Exercise 5: Working with Packages
Exercise 6: Lambda Functions
'''

#Task 1: Write a function that takes a list of numbers and returns the sum of the numbers.
'''
list1 = list()
sum = 0

num = int(input("Enter the number of inputs n list: "))

for i in range(num):
    print('Enter ind: ', i , ':', end=" ")
    list1.append(int(input()))
    sum = sum + list1[i]
    
print('Elements of list is: ', list1)
print('sum is: ', sum)
'''
#OR
'''
def listOfNum(list1):
    sum = 0
    for i in list1:
        sum = sum + i
    return sum

list1 = [10, 20, 30]
sum = listOfNum(list1)
print('Elements of list is: ', list1)
print('sum is: ', sum)
'''

#Task 2: Write a function that modifies a global variable and another function that uses a local variable 
#with the same name.
'''
VAR = 50
print("Globle VAR address: ", id(VAR))

def fun1():
    global VAR
    print("fun1 VAR address: ", id(VAR))
    VAR = 10
    print("fun1 VAR address: ", id(VAR))

def fun2():
    VAR = 20
    print("fun2 VAR address: ", id(VAR))
    return VAR
    
print('Global variable is: ', VAR, end="\n")
fun1()
print('update global variable by fun1: ', VAR, end="\n")
res = fun2()
print('Return local variable by fun2: ', res, end="\n")
'''

#Task 3: Write a script that uses the math module to calculate the area of a circle given its radius.
'''
import math

def calcAreaOfCircle(radius):
    print('PI value: ', math.pi)
    print('Radius square: ', math.pow(radius, 2))
    Area = math.pi * math.pow(radius, 2)
    return Area
    
rad = int(input("Enter the radius of Circle: "))
Area = calcAreaOfCircle(rad)
print("The area of circle of radius {:.2f}cm is: {:.2f}sq.cm".format(rad, Area))
'''

#Task 4: Create a custom module with a function that checks if a number is prime and use it in a script.
'''
import primeFile

objClass = primeFile.primeClass()
number = int(input("Enter a number: "))
res = objClass.primeFun(number)

if res==1:
    print("Number '{}' is 'Prime number'.".format(number))
else:
    print("Number '{}' is 'Not-Prime number'.".format(number))
'''

#Task 5: Create a package with multiple modules and use them in a script.
'''
import calculatorPack.addition
import calculatorPack.substraction
import calculatorPack.multiplication
import calculatorPack.division

cal = int(input('Press a number: 1: add, 2: sub, 3: mul, 4:div =>'))
n1 = int(input('Enter 1st num: '))
n2 = int(input('Enter 2nd num: '))

if cal==1:
    print(calculatorPack.addition.add(n1, n2))
elif cal==2:
    print(calculatorPack.substraction.sub(n1, n2))
elif cal==3:
    print(calculatorPack.multiplication.mul(n1, n2))
elif cal==4:
    print(calculatorPack.division.div(n1, n2))
else:
    print('Wrong input...!')
'''

#Task 6: Write a script that uses a lambda function to sort a list of tuples by the second element.
'''
def sortTuple(tup3):
    list3 = list(tup3)
    list3.sort()
    return tuple(list3)

resLamb = lambda tup2: sortTuple(tup2)

tup1 = (1,6,7,2,8,5,1,4,12,2)
print('tuple is: ', tup1)
print('Type is: ', type(tup1))

res = resLamb(tup1)

print('Sorted tuple is: ', res)
print('Type is result is: ', type(res))
'''
#OR
'''
resLamb = lambda tup2: tuple(sorted(tup2))

tup1 = (1,6,7,2,8,5,1,4,12,2)
print('tuple is: ', tup1)
print('Type is: ', type(tup1))

res = resLamb(tup1)

print('Sorted tuple is: ', res)
print('Type is result is: ', type(res))
'''

#=======================================================================================================================

#Session 4:

#Exercise 1: Reading from a Text File
'''
Task:
1.Open the File: Use the open() function to open a text file in read mode ('r'). Ensure to 
handle the file using a with statement for automatic closing.
2. Read the Content: Use the read() method to read the entire content of the file. 
Print the content to the console.
3. Error Handling: Handle potential exceptions such as FileNotFoundError and PermissionError.
'''
#code
'''
ses4_file = open('ses4_exe_file.txt', 'r')

try:
    with open('ses4_exe_fil.txt', 'r') as ses4_file:       # The file 'ses4_file.txt' is now closed automatically.
        readContent = ses4_file.read()
        print(readContent)
        
#except (FileNotFoundError):
    #print('File is not found: ', FileNotFoundError)
    
except (PermissionError):                                   #not getting it ***
    print('Permission is not availble: ', PermissionError)
    
except Exception as e:
    print('\n\nError is: ', e)
'''



#Exercise 2: Writing to a Text File
'''
Task:
1.Open the File: Use the open() function to open a text file in write mode ('w').
2.Write Content: Use the write() method to add a string to the file.
3. Error Handling: Handle potential exceptions that might occur during file operations.
'''

#code
'''
ses4_file = open('ses4_exe_file.txt', 'w')
print('File type, mode, encoding: ', ses4_file)

string = input("Write something here => ")
#string = "Write Content: Use the write() method to add a string to the file."

try:   
    #with open('ses4_exe_file.txt', 'w'):                   # This is also Working
    with open('ses4_exe_file.txt', 'w') as ses4_file:       # The file 'ses4_file.txt' is now closed automatically.
        ses4_file.writelines(string)
        
except (UnicodeEncodeError):                                  
    print('\n\nInvalide Unicode: ', UnicodeEncodeError)
    
except Exception as e:
    print('\n\nError is: ', e)
    
finally:
    with open('ses4_exe_file.txt', 'r') as ses4_file:      
        readContent = ses4_file.read()
        print("\nUpdated file content is => ", readContent)    
'''


#=========================================================================================================
''' 
हरे रामा, हरे रामा, रामा-रामा हरे हरे 
हरे कृष्णा, हरे कृष्णा, कृष्णा-कृष्णा हरे हरे 

Ye Duniya Ek Dulhan
Ye Duniya Ek Dulhan
Dulhan Ke Maathe Ki Bindiya
Ye Mera India
Ye Mera India
I Love My India
I Love My India
'''