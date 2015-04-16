#!python
"""
In the game, Monopoly, the standard board is set up in the following way:

GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
H2	 	C1
T2	 	U1
H1	 	C2
CH3	 	C3
R4	 	R2
G3	 	D1
CC3	 	CC2
G2	 	D2
G1	 	D3
G2J	F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP
A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL
Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.
The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
"""

import random

xxx = "GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL C1 U1 C2 C3 R2 D1 CC2 D2 D3 FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 G2J G1 G2 CC3 G3 R4 CH3 H1 T2 H2".split()
yyy = "00 01  02 03 04 05 06  07 08 09  10  11 12 13 14 15 16  17 18 19 20 21  22 23 24 25 26 27 28 29  30 31 32  33 34 35  36 37 38 39"  

CC = [0, 10, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
CH  = [0, 10, 11, 24, 39, 5, -1, -1, -2, -3, None, None, None, None, None, None]

v = [0 for i in range(40)]

d = [1, 2, 3, 4, ]

limit = 1000000

def next_rr(pos):
	if pos < 5:
		return 5
	if pos < 15:
		return 15
	if pos < 25:
		return 25
	if pos < 35:
		return 35
	return 5

def next_util(pos):
	if pos < 12:
		return 12
	if pos < 28:
		return 28
	return 12

def back_three(pos):
	pos -=3
	if pos < 0:
		pos += 40
	return pos

def modal_string():
	global v
	bs = list(reversed(sorted(v)))
	i, j, k = bs[:3]
	return "{0:0>2d}{1:0>2d}{2:0>2d}".format(v.index(i), v.index(j), v.index(k))

def resolve_CC(pos):
	global CC
	if pos in {2, 17, 33}:
		cc = random.choice(CC)
		if cc is not None:
			pos = cc
	return pos

def resolve_CH(pos):
	global CH
	if pos in {7, 22, 36}:
		ch = random.choice(CH)
		if ch is not None:
			if ch >= 0:
				pos = ch
			else:
				if ch == -1:
					pos = next_rr(pos)
				if ch == -2:
					pos = next_util(pos)
				if ch == -3:
					pos = back_three(pos)
	return pos

def resolve_G2J(pos):
	if pos == 30:
		return 10
	return pos

double_count = 0
pos = 0
for i in range(limit):
	a = random.choice(d)
	b = random.choice(d)
	if a==b:
		double_count +=1
	else:
		double_count = 0
	if double_count == 3:
		double_count = 0
		pos = 10 #go to jail
	else:
		pos = (pos + a + b)%40

	pos = resolve_G2J(resolve_CC(resolve_CH(pos)))
	v[pos]+=1
	print([i, modal_string()])

ss = sum(v)
for i in range(40):
	print([i, v[i]/ss])