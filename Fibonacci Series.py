#Take input from consol, keep it in List and print it
'''
lst = []

for i in range(5):
    lst.append(input("Enter the num for index: {} :-> ".format(i)))
    
print("\n",lst)
'''

#try switch-case in python
'''
def calculate(num, in1, in2):
    #print(num, in1, in2)
    if num is 1:
        return in1+in2
    elif num==2:
        return in1-in2
    elif num is 3:
        return in1/in2
    elif num==4:
        return in1*in2    
    else:
        print("Input not supported")
    
print("Enter the input sum:1, sub:2, div:3, mul:4 =>")
num = int(input())

print("Enter input 1:")
in1 = int(input())
print("Enter input 2:")
in2 = int(input())

result = calculate(num, in1, in2)
print(result)
'''

# Mutable - Link[] and String''
# Non-Mutable - Tuple()
# Dictionary - dict{}

'''
t1 = (10, 10, 6, 9)
print(t1)

n1 = t1.count(10)
print(n1)

n2 = t1.index(9)
print(n2)

#t1.append(8)     #Not-working
#print(t1)
'''
#CLASS

class Vehical:
    infoList = []
    
    def __init__(self, mName):
        ModelName = mName
        self.infoList.append(ModelName)
        print('save : ',ModelName)
        
    def wheelNum(self, wNum):
        wheelNum = wNum
        self.infoList.append(wheelNum)
        print('save : ',wheelNum)
        
    def enginName(self, eName):
        enginName = eName
        self.infoList.append(enginName)
        print('save : ',enginName)
        
    def display(self):
        return self.infoList


if __name__ == '__main__':
    veh1 = Vehical('BMW')
    
    veh1.wheelNum(4)
    veh1.enginName('cbw23')
    
    res = veh1.display()
    print('Vehcal details: ', res)
        













'''
#===========================================================================
#DICTIONARY:

dict1 = {'emp1':'balaji', 'emp2':'venkat'}
new1 = dict1.popitem()
print(new1)                 #remove and store last key and value in form of Tuple
print(dict1)                #remove last key and value (not store)

dict2 = {'name':'venkatprabu',
         'Id':'102',
         'company':'KnorrBremse'}
print('dict2: ',dict2)

new2 = dict2.pop('Id')          #Remove given key and store it into var
print(new2)
print('dict2: ',dict2)

dict3 = dict2.copy()            #Copy all dict2 into dict3
print('dict3: ',dict3)

dict3.clear()                   #Clear all
print('dict3: ',dict3)

print(dict2.fromkeys('name', 'Id'))     #

get1 = dict2.get('name')        #Read value and store it in given var. Not remove from dict2
print(get1)
print(dict2)

new3 = dict2.items()            #All item store in List
print(new3)

new4 = dict2.keys()             #All keys store in a List
print(new4)

dict2.setdefault('name')        #
print(dict2)

new5 = dict2.update()           #
print(new5)
print(dict2)

dict3 = {'name':'venkatprabu', 'details': {'Id':'102',
                                           'company':'KnorrBremse'}}
print(dict3)
new6 = dict3.popitem()
print(new6)                     #('details', {'Id': '102', 'company': 'KnorrBremse'})

#----------------------------------------------------------------------
#TUPLE:

print(new6)                     #('details', {'Id': '102', 'company': 'KnorrBremse'})
print(type(new6))

num1 = new6.count('details')
print(num1)

num2 = new6.index('details')
print(num2)


#----------------------------------------------------------------------
#SET


'''

