#! /usr/bin/python3
"""
The "-> float" is not necessary.
This part is calles type hint.
You can use it in conjunction with some tools like mypy.
It helps you to more robust code.
But it is not the same like java types. Python has stil a dynamic type reference.

"""
def example () -> float:
    return 1.2

"""
This if is like a main in java.
When this script invoked directly through shell
it will run the code below the if statement.
But when invoked as a module than the commands
below the if statement will not be invoked.
"""
if __name__ == "__main__":
    print(example())
