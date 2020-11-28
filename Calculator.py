import sys

def menu():
    print("\n\n                    Jayden's Brain Calculator")
    print()
    
    choice = input('''
                     A: Addition
                     B: Subtraction
                     C: Multiplication
                     D: Division
                     Q: Quit
                     
                     ENTER OPTION HERE: ''')
                     
    if choice == 'A' or choice == 'a':
        addition()
    elif choice == 'B' or choice == 'b':
        subtraction()
    elif choice == 'C' or choice == 'c':
        multiplication()
    elif choice == 'D' or choice == 'd':
        division()
    elif choice == 'Q' or choice == 'q':
        sys.exit(0)
    else:
        print('This is not a valid option\nPlease try again.')
        menu()
        
def addition():
    x = float(input('Insert first number: '))
    y = float(input('Insert second number: '))
    print(x+y)
    print('\n\n\n')
    menu()
    
def subtraction():
    x = float(input('Insert first number: '))
    y = float(input('Insert second number: '))
    print(x-y)
    print('\n\n\n')
    menu()
    
def multiplication():
    x = float(input('Insert first number: '))
    y = float(input('Insert second number: '))
    print(x*y)
    print('\n\n\n')
    menu()
    
def division():
    x = float(input('Insert first number: '))
    y = float(input('Insert second number: '))
    print(x/y)
    print('\n\n\n')
    menu()
    
    
menu()
