import feda_jakic_1, feda_jakic_2, feda_jakic_3

def main():
    flag = 1
    while(flag):
        print("Laboratorijska vjezba 1 - Feđa Jakić - fj127576")
        print("Enter number 1 for Task 1")
        print("Enter number 2 for Task 2")
        print("Enter number 3 for Task 3")
        print("Enter number 0 for EXIT")
        choice = int(input("Your choice: "))
        if(choice == 1):
            feda_jakic_1.main()
        elif(choice == 2):
            feda_jakic_2.main()
        elif(choice == 3):
            feda_jakic_3.main()
        elif(choice == 0):
            flag = 0
        print("EXIT")
    
if __name__ == '__main__':
    main() 