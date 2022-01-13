import pickle
def main():
    menu()
    

def menu():
    choice = 0
    print("---------------------------------------")
    print("|                 MENU                |") 
    print("---------------------------------------")
    print("|Enter (1) to add item                |\n|Enter (2) to display list            |")
    print("---------------------------------------")
    choice = int(input(" Enter a choice: "))
    print("")
    
    if choice == 1:
        additem()
    elif choice == 2:
        display()
    else:
        print("That is invalid try again")
        menu()

def additem():
    
    infile = open("TestFiles.txt", "at")

    date = input("Enter a date: ")
    task = input("Enter a task: ")
    infile.write(date + "\n")
    infile.write(task + "\n")
    infile.close()
    menu()
    
    
def display():
    infile = open("TestFiles.txt", "rt")
    date = infile.readline()
    print("-----------------------------------------")
    print("|              TODO LIST                |")
    print("-----------------------------------------")
    while date != "":
        task = infile.readline()
        date = infile.readline()
        date = date.rstrip('\n')
        task = task.rstrip("\n")

      
        #display
        print(f"|Date: {task}            Task: {date:8}|")
        print("-----------------------------------------")
        
        
    menu()

    
    





main()