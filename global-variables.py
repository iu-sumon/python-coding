# x = "awesome"  #This is global

# def myfunc():
#     print("Python is " + x)

# myfunc()

# x = "awesome" #This is global

# def myfunc():
#     x = "fantastic" # local variable is not global .It can only use in this function
#     print("Python is " + x)

# myfunc()

# print("Python is " + x)

# #--------------The global keyword------------------#
# # Rule-1
# def myfunc():
#     global x
#     x = "fantastic" #this is global

# myfunc()

# print("Python is " + x)

# Rule-2
x = "awesome"

def myfucn():
    global x #when any variable declare by global keyword. It will be global variable.
    x= "fantastic"

myfucn()

print("Python is " + x)


