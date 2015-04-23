#!python
"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

def is_increasing(n):
	return n==int("".join(sorted(list(str(n)))))

def is_decreasing(n):
	return n==(int("".join(reversed(sorted(list(str(n)))))))

def is_bouncy(n):
	return not is_increasing(n) and not is_decreasing(n)

target = .99

bouncy_count = 0
ttl_count=99

ratio = 0

while ratio < target:
	ttl_count += 1
	if is_bouncy(ttl_count):
		bouncy_count+=1
	ratio = bouncy_count / ttl_count

print(ttl_count)


