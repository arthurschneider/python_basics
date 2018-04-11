#! /usr/bin/python3

condition = 1

'''
You can use alos while True:
    this will crate an infinit loop
    to break it you have to ^C
'''

print("----------while loop until 10---------------------")
while condition < 10:
    print(condition)
    condition +=1

print("----------while loop backwards---------------------")

condition = 9
while condition > 0:
    print (condition)
    condition -=1


print("----------for loop with a list---------------------")

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    print (number)


print("----------for loop with a range---------------------")

for x in range(1,10):
    print(x)

print("----------for loop with a backward range---------------------")

for x in range(9,0, -1):
    print(x)
