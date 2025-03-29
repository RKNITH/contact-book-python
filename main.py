import numpy as np
import pandas as pd
from def_for_contacts import *




run = True
while run == True:
    print('''What you want to do :-
    new     -- make a new contacts
    save    -- save the current changes
    see     -- see full list
    search  -- search a Number
    remove  -- delete a Number
    exit    -- exit program ''')
    do = str(input(":"))
    print("----------"*10)
    if do == 'new':
        add()
        print("----------"*10)
    if do == 'save':
        print("Saving the file.....")
        save()
        print("saved file :-")
        print(main)  
        print("----------"*10)
    if do == 'see':
        see()
        print("----------"*10)
    if do == 'exit':
        run = False
        print("----------"*10)
    if do == 'search':
        search()
        print("----------"*10)
    if do == 'remove':
        remove()
        print("----------"*10)

