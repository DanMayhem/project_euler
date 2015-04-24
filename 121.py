#!python
"""
A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.

The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.

If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given the player actually wins £9.

Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.
"""

from itertools import product
from fractions import Fraction

turns = 15

odds_per_turn = [(i+2) for i in range(turns)]
print(odds_per_turn)

win_ways = 0
lose_ways = 0

for game in product("RB",repeat=turns):
	ways = 1
	for i in range(len(game)):
		if game[i]=="R":
			ways *= odds_per_turn[i]-1
		else:
			ways *= 1
	if game.count("B")>game.count("R"):
		win_ways += ways
		print(["W", game, ways])
	else:
		lose_ways += ways
		print(["L", game, ways])
		

print([win_ways, lose_ways, win_ways + lose_ways, str(Fraction(win_ways, win_ways+lose_ways)), (win_ways+lose_ways)//win_ways])
