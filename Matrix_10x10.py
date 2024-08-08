
class matrix:
    def __init__(self):
        self.row = None
        self.coloumn = None
        self.mat = []
        
    def input(self, row, coloumn):
        if (row > 10 or coloumn > 10) and (row < 1 or coloumn < 1):
            print("Exceeded limits of 10")
            #raise OverflowError 
        else:
            self.row = row
            self.coloumn = coloumn
            self.createMatrix()

    def createMatrix(self):
        for r in range(self.row):
            temp = []
            for c in range(self.coloumn):
                temp.append(00)                                                                                                                                                                                                                          
            self.mat.append(temp)
            
    def printMatrix(self):
        #print(self.mat)
        print("\n")
        for i in self.mat:
            print(" "*20, "|", end=" ")
            for j in i:
                if j<10:
                    print("0{}".format(j), end=" ")
                else:
                    print(j, end=" ")
            print("|")
        print("\n")
        
    def addElement(self, r1, c1):   
        self.mat[r1][c1] = int(input(f'\nEnter the value of Matrix[{r1},{c1}] : '))  
        self.printMatrix()
        
    def updateElement(self):
        r1 = int(input("Enter the row number: "))
        c1 = int(input("Enter the coloumn number: "))
        self.addElement(r1, c1)
    

matObj = matrix()

matObj.input(7, 9)
matObj.printMatrix()

matObj.updateElement()


        



    