def printNumberTriangle(maxNumber):
    maxRowValueIter = 1
    printNum = 1
    for i in range(1, maxNumber+1):
        flagForSubstraction = 1
        print()
        printNum = i
        for row in range(1, maxRowValueIter + 1):
            print(printNum % 10, end=" ")
            if(printNum == maxRowValueIter):
                printNum -= 1
                flagForSubstraction = 0
            elif(flagForSubstraction and printNum < maxRowValueIter):
                printNum += 1
            else:
                printNum -= 1
        maxRowValueIter += 2

             
def secondTask():
    maxNumber = int(input("Insert integer: "))
    
    if(maxNumber > 20):
        return
    else:
        printNumberTriangle(maxNumber)
   