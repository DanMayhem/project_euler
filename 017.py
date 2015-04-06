#!python
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

from math import floor

def number_to_words(n):
  ones_dict = {
    0:"",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen"
  }
  tens_dict = {
    0:"",
    2:"twenty",
    3:"thirty",
    4:"forty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"ninety"
  }
  if n == 1000:
    return "onethousand"
  if n in range(100,1000):
    tenspart = number_to_words(n%100)
    if len(tenspart) > 0:
      tenspart = "and"+tenspart
    return number_to_words(floor(n/100))+"hundred"+tenspart
  if n in range(20,100):
    return tens_dict[floor(n/10)] + ones_dict[n%10]
  if n in range(1,20):
    return ones_dict[n]
  return ""

if __name__=="__main__":
  l = 0
  for i in range(1001):
    print("%d:%s"%(i,number_to_words(i)))
    l += len(number_to_words(i))
  print(l)

