LIST: 
    
lis2 = list()       #-to create list
lis1 = []

lis = [5,6,5,2,5]   #-to insert list
print(lis)
[5, 6, 5, 2, 5]

lis.append(2)
lis.append(8)       #-at last
print(lis)
[5, 6, 5, 2, 5, 2, 8]

lis.remove(2)       #-remove 1st value (2)
print(lis)
[5, 6, 5, 5, 2, 8]

lis.clear()         #-clear all
print(lis)
[]                  

lis = [5,6,5,2,5]
lis2 = list()

lis2 = lis.copy()   #-copy lis to lis2
print(lis2)
[5, 6, 5, 2, 5]

lis2.pop()          #-to remove last value of list
5
print(lis2)
[5, 6, 5, 2]

lis2.reverse()      #-reverse the list
print(lis2)
[2, 5, 6, 5]

lis2.sort()         #-to sort the list
print(lis2)
[2, 5, 5, 6]

lis3 = []
print(lis3)
[]
lis3.extend(lis2)   #-to copy lis2 to lis3
print(lis3)
[2, 5, 5, 6]

ind_of_5 = lis3.index(5)    #-Returns the index of the first matched item
print(ind_of_5)
1

count_of_5 = lis3.count(5)  #-Returns the count of the number of items passed as an argument
print(count_of_5)
2

#=========================================================================

list1 = [2, 5, 5, 6, 2]
Max_ele = max(list1)        #-return maximum element of a given list
print(Max_ele)
6
min_ele = min(list1)        #-return minimum element of a given list
print(min_ele)
2
length = len(list1)         #-Returns length of the list or size of the list
print(length)
5
any_one = any(list1)        #-return true if any element of the list is true. if the list is empty, return false
print(any_one)
True
list2 = [0,0,0,0]   -False
list2 = [0,0,0,0,1] -True

#=========================================================================
SLICING:    +1:[->] or -1:[<-]

         
list1 = [10,20,30,40,50,60,70,80,90,100]

print(list[3])
list[3]
print(list1[1:3])
[20, 30]
print(list1[::2])
[10, 30, 50, 70, 90]
print(list1[2:8:2])
[30, 50, 70]

print(list1[-2])
90
print(list1[2:8:-1])
[]
print(list1[8:2:-1])
[90, 80, 70, 60, 50, 40]
print(list1[-4:-9:-1])
[70, 60, 50, 40, 30]
print(list1[-4:-9:-2])
[70, 50, 30]

str = "abcdefghij"

print(str[1])
b
print(str[-1])
j
print(str[4:8])
efgh
print(str[2:7:1])
cdefg
print(str[8:2:-1])
ihgfed
print(str[8:2:-1])

#=========================================================================
STRING:
    
name = 'ashish'
id=10
str1 = f'my name is {name} and my id is {id}'

print(str1)
my name is ashish and my id is 10

print(f'my name is {name} and my id is {id}')
my name is ashish and my id is 10

print('my name is %s and my id is %d' %(name , id))
my name is ashish and my id is 10

print('my name is {} and my id is {}'.format(name , id))
my name is ashish and my id is 10

print('my name is {1} and my id is {0}'.format(name , id))
my name is 10 and my id is ashish

print('{:f}|{:5f}|{:8.2f}|{:2.0f}|{:d}|{:<5d}|{:>5d}|{:>12.3f}|'.format(id,id,id,id,id,id,id,id))
10.000000|10.000000|   10.00|10|10|10   |   10|      10.000|

#------------------------------------------------------------------
str1 = 'ashish'

str1.capitalize()       -1st letter capitalize
'Ashish'

str1.swapcase()
'ASHISH'

#------------------------------------------------------------------





