# List operations Project
import os
import msvcrt as msv
import sys
lst = []
def addElement(lst):
    os.system("cls")
    print("Insert New Element Module Called... \n")
    data = input("Enter New Element --- ")
    print("\nAre you sure you want to add new element or not, if yes press 1 else any key... ")
    c = msv.getch().decode()
    if c == '1':
        lst.append(data)
        print("\nData Successfully inserted.. \n")
   
    print("\nDo you want to add any more records, press 1 and for going to main menu press 2... ")
    c = msv.getch().decode().upper()
    if c == '1':
        addElement(lst)
    elif c == '2':
        return
def showElement(lst):
    os.system("cls")
    print("Showing the list module called....  \n")
    if len(lst)==0:
        print("List is empty!! Please insert elements from module 1\n\n")
    else:
        print("\nAre you sure to print the list; if yes, press 1 else any key")
        c=msv.getch().decode()
        if c == "1":
            print(lst)
def delete(lst):
    os.system("cls")
    print("\nDeleting the element module called... \n")
    if len(lst)==0:
        print("List is empty!! Please insert elements from module 1\n\n")
    else:
        elem = input("\nEnter element to delete --- ")
        if elem in lst:
            print("\nAre you sure you want to delete this element? Press 1 to confirm...")
            c = msv.getch().decode()
            if c == '1':
                lst.remove(elem)
                print("\nElement deleted successfully.\n")
        else:
            print("\nElement not found in list.\n")
        print("\nDo you want to delete more elements? Press 1 else 2...")
        c = msv.getch().decode().upper()
        if c == '1':
            delete(lst)
        elif c == '2':
            return
def search(lst):
    os.system("cls")
    print("Searching the element module called... \n")
    if len(lst)==0:
        print("List is empty!! Please insert elements from module 1\n\n")
    else:
        elem=input("\nEnter the element you want to search in the list -- ")
        if elem in lst:
            print(f"Element is at index number {lst.index(elem)+1}")
        else:
            print("\nElement not found in the list\n")
        print("\nDo you want to find more elements? Press 1 else 2...")
        c = msv.getch().decode().upper()
        if c == "1":
            search(lst)
        elif c == "2":
            return
def sort(lst):
    os.system("cls")
    print("\nSorting the list module called... \n")
    if len(lst)==0:
        print("\nList is empty, enter atleast 2 elements\n")
    elif len(lst)==1:
        print("\nCannot sort a list with 1 element, enter atleast 2 elements \n")
    else:
        print("\nAscending order -> 1 , Descending order -> 2\n")
        c = msv.getch().decode()
        if c == '1':
            lst.sort()
            print(lst)
        elif c == '2':
            lst.sort(reverse=True)
            print(lst)
def update(lst):
    os.system("cls")
    print("\nUpdating the list module called... \n")
    if len(lst)==0:
        print("List is empty!! Please insert elements from module 1\n\n")
    else:
        index=input("Enter the index at which you want to update -- ")
        if index.isdigit():
            index=int(index)
            if index>=0 and index<10:
                new=input("\nEnter new element to update -- ")
                print("\nPress 1 to confirm update...")
                c = msv.getch().decode()
                if c == '1':
                    lst.insert(index, new)
                    print("Updated List :", lst)
            else:
                print("\nList index out of range")
        else:
            print("\nEnter index in numbers")
        print("\nDo you want to update more elements? Press 1 else 2...")
        c = msv.getch().decode().upper()
       
        if c == '1':
            update(lst)
        elif c == '2':
            return
def count_one(lst):
    os.system("cls")
    print("\nCounting single element occurrence module called...\n")
    if len(lst)==0:
        print("List is empty!! Please insert elements from module 1\n\n")
    else:
        elem = input("Enter the element you want to count -- ")
        count = lst.count(elem)
        print(f"\nElement '{elem}' occurs {count} time(s) in the list.\n")
       
        print("Do you want to count another element? Press 1 else 2...")
        c = msv.getch().decode().upper()
        if c == '1':
            count_one(lst)
        elif c == '2':
            return
def count_all(lst):
    os.system("cls")
    print("\nCounting all element occurrence module called...\n")
    if len(lst)==0:
        print("List is empty!! Please insert elements from module 1\n\n")
    else:
        element=[]
        for i in lst:
            if i not in element:
                element.append(i)
        count = {}
        for item in element:
            count[item] = lst.count(item)
       
        for item, cnt in count.items():
            print(f"{item} ---> {cnt}")
def MainModule():
    os.system("cls")
    print("List Operation Project --- \n")
    print('''
    1 -> Add item
    2 -> Show item
    3 -> Delete item
    4 -> Search item
    5 -> Sort item
    6 -> Update list
    7 -> Count 1 element occurence
    8 -> Count all element occurence
    9 -> Exit
    ''')
    while True:
        c = msv.getch().decode()
        if c == '1':
            addElement(lst)
       
        elif c == "2":
            showElement(lst)
       
        elif c == '3':
            delete(lst)
       
        elif c == '4':
            search(lst)
       
        elif c == '5':
            sort(lst)
       
        elif c == '6':
            update(lst)
       
        elif c == '7':
            count_one(lst)
       
        elif c == '8':
            count_all(lst)
       
        elif c == '9':
            os.system("cls")
            print("\nExiting the program... Thank you!\n")
            sys.exit(0)
           
        print("\n\nDo you want to continue... press 1 else any key.... ")
        c = msv.getch().decode()
        if c == '1':
            MainModule()
MainModule()




