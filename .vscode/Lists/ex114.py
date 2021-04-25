from random import randint

def rand_lot():
    newlist = list()
    while len(newlist) != 6:
        add = randint(1,49)
        if not add in newlist:
            newlist.append(add)
    return sorted(newlist)


print(*rand_lot(), sep=' ')


#You are working on a big project
#and it works and you want to do 
#something new and you occur new
#bugs. How to fix?
#1. Start w/ a Pseudocode
#2. Use Python Debugging system
#3. Shift the function to a new project and fix it from there
#4. Reconsider where to implement the new item 