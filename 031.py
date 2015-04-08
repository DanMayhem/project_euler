#!python
"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

from math import floor

values=[200, 100, 50, 20, 10, 5, 2, 1]

def purse_generator(target, coins):
	if len(coins)==1:
		yield [target] #assumes the last coin is always value 1
	else:
		for i in range(floor(target/coins[0])+1):
			for purse in purse_generator(target-coins[0]*i, coins[1:]):
				yield [i] + purse


if __name__=="__main__":
	c=0
	for p in purse_generator(200, values):
		print(p)
		c+=1

	print(c)