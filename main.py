menuOption = None

mylist = []

menuText = '''
1.) Add item
2.) Print list
3.) Remove item by number
4.) Save list to file
5.) Load list from file
6.) Exit
'''

while menuOption != '6':
    print(menuText)
    menuOption = input("Enter selection\n")
    print(menuOption)
    if menuOption == '1':
        print("Add item")
        temp = input("Enter item\n")
    elif menuOption == '2':
        print("Print list")
    else:
        print("Your selection was not recognized.")
        
    