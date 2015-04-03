#!python
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


from functools import reduce

numbers = range(1,1000)

threes = set(filter(lambda x: x%3==0, numbers))

fives = set(filter(lambda x: x%5==0, numbers))

u = threes | fives

s = reduce(lambda x, y: x+y, u)

print(s)