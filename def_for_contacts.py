import numpy as np
import pandas as pd


main = np.load("contacts.npy")

def add():
    global main
    
    name = str(input("write name :"))
    num = int(input("write number :"))
    add_array = np.array([name,num])
    print(add_array)
    main = np.vstack((main,add_array))
    print('Number is added to list')
    return main


def save():
    np.save("contacts",main)

    df = pd.DataFrame(main)
         ##save to xlsx file
    filepath = 'excel_contacts.xlsx'
    df.to_excel(filepath, index=False)

    print("Saved seccecfully")

def see():
    print(main)

def search():
    s = list(main[:,0])
    n = str(input("Type name :"))
    for i,elem in enumerate(s):
        if n in elem :
            no = s.index(elem)
            print(main[no,0]," -- ",main[no,1])


def remove():
    global main
    main_list = list( main[ :, 0])
    remove_name = str( input("Search a name to remove :"))
    
    for i,elem in enumerate( main_list):
        if remove_name in elem :
            elem_no = main_list.index( elem)
            print( main[elem_no, 0]," -- ",main[elem_no, 1])

    full_remove_name = str(input("Type full name to remove :"))
    if full_remove_name in main_list:
        index_no_to_remove = main_list.index( full_remove_name)
        main = np.delete(main, index_no_to_remove, 0)
        print(main)
        
    




            