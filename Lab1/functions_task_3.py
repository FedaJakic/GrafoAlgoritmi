def getAllPrimeNumbersBetweenTwoDecimal(decimalRange):
    i = round(decimalRange[0])
    for i in range(0, round(decimalRange[1]) - round(decimalRange[0])):
        if(checkIsPrime(i)):
            print(i, " is prime number!")
        else:
            continue
        
def getNPrimeNumber(nNumber):
    primeCounter = 0
    for i in range(2,1000):
        if(checkIsPrime(i)):
            primeCounter += 1
        
        if(primeCounter == nNumber):
            print(nNumber, " number that is prime is: ", i)
            break
        
def getNeighboringPrimeNumbers(nNumber):
    lastPrime = 1
    for i in range (2, nNumber):
        if(checkIsPrime(i)):
            if((i-lastPrime) == 2):
                print("[ ", lastPrime, " , ", i, " ]")
            lastPrime = i
            
def getPrimeNumberSum(nNumber):
    primeNumbers = []
    for i in range (2, nNumber):
        if(checkIsPrime(i)):
            primeNumbers.append(i)
    
    i = 0
    j = len(primeNumbers) -1
    
    while(i < j):
        if(primeNumbers[i] + primeNumbers[j] == nNumber):
            print(primeNumbers[i], " + ", primeNumbers[j], " = ", nNumber)
            print(primeNumbers[j], " + ", primeNumbers[i], " = ", nNumber)
            i += 1
            j -= 1
        elif(primeNumbers[i] + primeNumbers[j] < nNumber):
            i += 1
        else:
            j -= 1
            
        
def checkIsPrime(data):
    primeCounter = 0
    for i in range (1, data + 1):
        if(data % i == 0):
            primeCounter += 1
    
    if(primeCounter == 2):
        return True
    else:
        return False    

def thirdTask():
    print("(a)")
    decimalRange = []
    for i in range (0, 2):
        decimalRange.append(float(input("Insert decimal number: ")))
    decimalRange.sort()
    getAllPrimeNumbersBetweenTwoDecimal(decimalRange)
    print("(b)")
    nNumber = int(input("Insert n number: "))
    if(nNumber < 1):
        print("Only positive integers")
    else:
        getNPrimeNumber(nNumber)
    print("(c)")
    nNumber = int(input("Insert n number: "))
    if(nNumber < 1):
        print("Only positive integers")
    else:
        getNeighboringPrimeNumbers(nNumber)
    print("(d)")
    nNumber = int(input("Insert even n number: "))
    if(nNumber < 1 or nNumber % 2 != 0):
        print("Only positive even integers")
    else:
        getPrimeNumberSum(nNumber)
    
# Testing
def testing():
    if(checkIsPrime(11)):
        print("checkIsPrime(11) Test passed!")
    else:
        print("checkIsPrime(11) Test failed!")
    if(checkIsPrime(25)):
        print("checkIsPrime(25) Test failed!")
    else:
        print("checkIsPrime(25) Test passed!")
        
if __name__ == '__main__':
    testing() 