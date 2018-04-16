#! /usr/bin/python3
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
