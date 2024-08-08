
class matrix:
    matrixflag = 3
    def __init__(self):
        self.row = None
        self.coloumn = None
        self.mat = []
        
    def input(self):
        self.matrixflag -= 1
        self.row = int(input("Enter number of row: "))
        self.coloumn = int(input("Enter number of coloumn: "))
        
        if (self.row <= 10 and self.coloumn <= 10) and (self.row >= 1 and self.coloumn >= 1):
            self.createMatrix()        
        else:
            if self.matrixflag > 0:
                print(f"\nExceeded limits of row and coloumn \nTry again... you have last {self.matrixflag} chance\n")
                self.input()
            else:
                print("\nYou Exceeded the all 3 chances...\n", "_"*100)
            #raise OverflowError 
            

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
        print("Update the Matrix element")
        r1 = int(input(f"\tEnter the row number(0-{self.row-1}): "))
        c1 = int(input(f"\tEnter the coloumn number(0-{self.coloumn-1}): "))
        self.addElement(r1, c1)
    

matObj = matrix()

matObj.input()
matObj.printMatrix()

num=1
while(num == 1):
    matObj.updateElement()
    num = input("Are you want to update again! \n\tPress 1: for update\n\tPress 0: for not update\n")


        



    