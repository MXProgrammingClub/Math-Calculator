def factorization(num):
    if isinstance(num, (str, float)):
        print("error, inputted value is not an integer")
    else:
        factors = []
        import math
        test = num
        while test > 1:
            mod = num%test
            if mod == 0:
                factors.append(test)
            test -=1
        print (factors)

def Greatest(num1, num2):
    if isinstance(num1 or num2, (str, float)):
        print("error, one or more inputted values is not an integer")
    else:
        import math
        GCDnum = 1
        num1Mult = num1-1
        num2Mult = num2-1
        factors = []
        factorNum = num1-1
        if num1%num2 == 0 or num2%num1 == 0:
            if num1<=num2:
                print ("The greatest common denominator is: ")
                print (num1)
            else:
                print ("The greatest common denominator is: ")
                print (num2)
        else:
            while num1Mult > 1:
                mod = num1%num1Mult
                if mod == 0:
                    factors.append(num1Mult)
                num1Mult -=1
            
            while num2Mult > 1:
                mod = num2%num2Mult
                if mod == 0:
                    factors.append(num2Mult)
                num2Mult -=1
            while GCDnum == 1:
                if factors.count(factorNum) == 2:
                    GCDnum = factorNum
                else:
                    factorNum-=1
                    
            print ("The greatest common multiple is :")
            print (GCDnum)

def Least(num1, num2):
    if isinstance(num1 or num2, (str, float)):
        print("error, one or more inputted values is not an integer")
    else:
        import math
        LCM = 0
        if num1>= num2:
            test = num1
        else:
            test = num2
        while LCM == 0:
            if test%num1 ==0 and test%num2 == 0:
                LCM = test
            else:
                test +=1
            
        print("The least common multiple is: ")
        print(LCM)

def dotProduct(list1, list2):
    import math
    i=0
    num1 = 0
    num2 = 0
    product = 0
    if isinstance(list1 or list2, (list)):
        if len(list1) != len(list2):
            return("it is not possible to take the dot product of your vectors")
        else:
            while i < len(list1):
                num1 = list1[i]
                num2 = list2[i]
                product += num1*num2
                i+=1
    else:
        return("error, one or more of your entries is not a list")
    return product


def crossProduct(list1, list2):
    import math
    crossProduct = []
    num1 = 0
    num2 = 0
    num3 = 0
    if isinstance(list1 or list2, (list)):
        if len(list1) != 3 or len(list2) != 3:
            return("it is not possible to take the cross product of your vectors")
        else:
            num1= list1[1]*list2[2]-list1[2]*list2[1]
            num2= list1[2]*list2[0]-list1[0]*list2[2]
            num3= list1[0]*list2[1]-list1[1]*list2[0]
            crossProduct.append(num1)
            crossProduct.append(num2)
            crossProduct.append(num3)
            
    else:
        return("error, one or more of your entries is not a list")
    return crossProduct
