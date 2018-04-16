#! /usr/bin/python3


def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply_by(number1, number2):
    return number1*number2

def divide(number1, number2):
    return number1/number2


def simple(num1, num2):
    print("1 :", num1, "2 :", num2)
    pass

def simple(num1, num2=3):
    print("1 :", num1, "2 :", num2)
    pass

def basic_window(width, heigth, font="TNR", backGroundColor="white"):
    print(width, heigth, font,backGroundColor)

if __name__=="__main__":
    number1 = 5
    number2 = 2
    black="black"

    print(number1,"+",number2,"=",add(number1,number2))
    print(number1,"-",number2,"=",subtract(number1,number2))
    print(number1,"-",number2,"=",subtract(number2=number1, number1=number2))
    print(number1,"*",number2,"=",multiply_by(number1,number2))
    print(number1,"/",number2,"=",divide(number1,number2))
    print("Called simple function return is", simple(number1, number2))
    print("Called simple function return is", simple(number1))
    basic_window(800,600)
    basic_window(800,600, "Arial")
    basic_window(800,600, backGroundColor=black)
