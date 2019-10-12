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

Greatest(2993,2324)
