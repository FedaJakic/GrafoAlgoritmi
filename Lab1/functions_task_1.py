#Functions
def isPythagoreanTheorem(pythagoreanList):
    pythagoreanList.sort()
    
    if((pythagoreanList[0] ** 2) + (pythagoreanList[1] ** 2) == (pythagoreanList[2] ** 2)):
        return True
    else:
        return False
    
def firstTask():
    print("1. Task")
    pythagoreanList = []
    
    for i in range (1,4):
        pythagoreanList.append(int(input("Insert integer: ")))
        if(pythagoreanList[i-1] <= 0):
            print("End of Program")
            return
        
    if(isPythagoreanTheorem(pythagoreanList)):
        print("Numbers are valid!")
    else:
        print("Numbers are NOT valid!")

# Testing
def testing():
    if(isPythagoreanTheorem([3,4,5])):
        print("1. Test passed!")
    else:
        print("1. Test failed!")
    if(isPythagoreanTheorem([2,3,4])):
        print("2. Test failed!")
    else:
        print("2. Test passed!")
    if(isPythagoreanTheorem([5,3,4])):
        print("3. Test passed!")
    else:
        print("3. Test failed!")
        
if __name__ == '__main__':
    testing() 
        