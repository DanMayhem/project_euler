#!python
"""
Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, and so on. But there are nine 4-digit primes containing three ones:

1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime where d is the repeated digit, N(n, d) represents the number of such primes, and S(n, d) represents the sum of these primes.

So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit, there are N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275. It turns out that for d = 0, it is only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.

In the same way we obtain the following results for 4-digit primes.

Digit, d  M(4, d) N(4, d) S(4, d)
0 2 13  67061
1 3 9 22275
2 3 1 2221
3 3 12  46214
4 3 2 8888
5 3 1 5557
6 3 1 6661
7 3 9 57863
8 3 1 8887
9 3 7 48073
For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d).
"""

from functools import lru_cache
from itertools import combinations_with_replacement, permutations, combinations

from pe import is_prime

limit = 10
digits = list(map(int, list("0123456789")))

@lru_cache(maxsize=None)
def is_prime_c(n):
  return is_prime(n)

def _has_repeated_digit(x, d):
  return str(x).count(str(d))>1

def mns(x, d):
  m = 0
  n = 0
  s = 0
  for i in range(10**(x-1),10**x):
    mm = str(i).count(str(d))
    if mm > m:
      if is_prime_c(i):
        m=mm
        n=0
        s=0
    if mm == m:
      if is_prime_c(i):
        n+=1
        s+=i
  return (m, n, s)
      

def _fill_candidate(c, n, d):
  """
    return every combination of the candidate c, padded
    to length n with digit d
  """
  if n == 0:
    yield c
    return
  for i in range(len(c)+1):
    if not(i > 0 and c[i-1]==d):
        cc = c[:i]+d+c[i:]
        for x in _fill_candidate(cc, n-1, d):
          yield x

def generate_candidates(d, n):
  n = limit-n
  for i in range(10**n):
    i = str(i)
    while len(i) < n:
      i = "0"+i
    if i.count(str(d))==0:
      for c in _fill_candidate(i, limit-len(str(i)), str(d)):
        if c[0]!='0':
          yield int(c)

ss = 0
for run_dig in digits:
  m = 0
  n = 0
  s = 0
  run_len = limit - 1
  while m==0 and run_len > 1:
    for c in set(generate_candidates(run_dig, run_len)):
      if is_prime_c(c):
        m = run_len
        n += 1
        s += c
        ss += c
    run_len -= 1
  print([limit, run_dig, m, n, s])
print(ss)

