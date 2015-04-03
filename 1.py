#!python

from functools import reduce

numbers = range(1,1000)

threes = set(filter(lambda x: x%3==0, numbers))

fives = set(filter(lambda x: x%5==0, numbers))

u = threes | fives

s = reduce(lambda x, y: x+y, u)

print(s)