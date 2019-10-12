
def convert(baseFrom, baseTo, number):
    #note: this function does not check that the number is valid in the given base
    #note2: baseFrom and BaseTo must be within the inclusive range [2, 36]
    alphaToNum = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15, 'g':16, 'h':17,
                  'i':18, 'j':19, 'k':20, 'l':21, 'm':22, 'n':23, 'o':24, 'p':25,
                  'q':26, 'r':27, 's':28, 't':29, 'u':30, 'v':31, 'w':32, 'x':33, 'y':34, 'z':35}
    numToAlpha = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 
                  18:'I', 19:'J', 20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 25:'P',
                  26:'Q', 27:'R', 28:'S', 29:'T', 30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}
    stringed = str(number)
    decRes = int(stringed, baseFrom)
    highExpo = 0


    while baseTo**highExpo <= decRes:
        highExpo +=1
    listRes = []
    for exp in reversed(range(0, highExpo)):
        curCoef = 1
        if(baseTo**exp <= decRes):
            while(curCoef*baseTo**exp <= decRes):
                curCoef += 1
            curCoef-=1
            decRes -= curCoef*baseTo**exp
            if curCoef >= 10:
                curCoef = numToAlpha[curCoef]
            listRes.append(str(curCoef))
        else:
            listRes.append('0')
    strRes = ''
    for w in listRes:
        strRes += w   
        return strRes


def calculate(numbers, operations, bases, baseRes):
    #all parameters must be lists, and len(numbers) == len(bases) == len(operations) + 1 must be true
    for i in range(0, len(numbers)):
        numbers[i] = int(convert(bases[i], 10, numbers[i]))
    ops_left = True
    while ops_left:
        ops_left = False
        for i in range(0, len(operations)):
            if(operations[i] == '*'):
                numbers[i] = numbers[i] * numbers[i+1]
                del numbers[i + 1]
                del operations[i]
                ops_left = True
                break
            if(operations[i] == '/'):
                numbers[i] = numbers[i] / numbers[i + 1]
                del numbers[i + 1]
                del operations[i]
                ops_left = True
                break
    while len(operations) > 0:
        for i in range(0, len(operations)):
            if(operations[i] == '-'):
                numbers[i] = numbers[i] - numbers[i + 1]
                del numbers[i + 1]
                del operations[i]
                break
            if(operations[i] == '+'):
                numbers[i] = numbers[i] + numbers[i + 1]
                del numbers[i + 1]
                del operations[i]
                break
    return convert(10, baseRes, int(numbers[0] + .5))

convert(2, 10, "A2")