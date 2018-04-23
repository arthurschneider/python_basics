#! /usr/bin/python3

import statistics

example_list = [3,4,2,8,8,5,9,6,7,3]

x = statistics.mean(example_list)
print(x)


y = statistics.median(example_list)
print(y)


#z = statistics.mode(example_list)
#print(z)


a = statistics.stdev(example_list)
print(a)


b = statistics.variance(example_list)
print(b)
