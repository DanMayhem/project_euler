#!python
"""
The most naive way of computing n15 requires fourteen multiplications:

n × n × ... × n = n15

But using a "binary" method you can compute it in six multiplications:

n × n = n2
n2 × n2 = n4
n4 × n4 = n8
n8 × n4 = n12
n12 × n2 = n14
n14 × n = n15

However it is yet possible to compute it in only five multiplications:

n × n = n2
n2 × n = n3
n3 × n3 = n6
n6 × n6 = n12
n12 × n3 = n15

We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.

For 1 ≤ k ≤ 200, find ∑ m(k).
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def m(k):
	if k == 1:
		return 0
	mm = k
	for i in range(1,k):
		if 2*i ==k:
			mmm = m(i) + 1
		else:
			mmm = m(i) + m(k-i) + 1
		if mmm < mm:
			print([k, i, k-i])
			mm = mmm
	return mm

print(m(15))