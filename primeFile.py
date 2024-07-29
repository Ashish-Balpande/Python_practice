
class primeClass:
    def primeFun(self, num):
        flag = False
        
        if num==1:
            flag = True
        elif num>1:
            for i in range(2, num):
                if (num%i == 0):
                    flag = False
                    break
                else:
                    flag = True
        else:
            flag = False
        
        return flag
    
