

class class1:
    def __init__(self):
        self.didID = None
        self.didName = None
        
    def set(self, id1, name1):
        self.didID = id1
        self.didName = name1
        
    def get(self):
        lst1 = []
        lst1.append(self.didID)
        lst1.append(self.didName)   
        return lst1
        
    def getAshish(self):
        return self.didID, self.didName

classObj = class1()

classObj.set(123, "ashish")

res = classObj.get()
print(res)
res1 = classObj.getAshish()
print(res1)

