#! /usr/bin/python3

"""
This is not a global variable
it only has no parent function.
You can think of it like a redable global variable
"""
x = 7

def print_the_x():
    """
    You can print out x and add a number in print function
    But you cannot assign
    """
    print(x)
    print(x+2)

    """
    This is now allowed because it is not a local variable,
    it is not allowed to modify the global variable
    """
    # x+=6

def print_and_modify_global_variable():
    # This statement defines a global variable
    global x

    print(x)
    x+=4
    print(x)

def print_x_but_not_as_global():
    """
    Here you assign x to a local variable
    and because it is allowed to modify local variables
    you can print and work with the new variable
    BUT x will not be modified
    """
    globx = x
    print(globx)
    globx+=2
    print(globx)
    print(x)

def modify_x(modify):
    print(modify)
    modify+=66
    print(modify)
    return modify


if __name__== "__main__":
    print_the_x()
    print_and_modify_global_variable()
    print("x after defining global and modifying it",x)
    print_x_but_not_as_global()
    x = modify_x(x)
    print(x)
