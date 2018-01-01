# Runs as is for python 2.7 interpreter.
# prime_factors prints the prime factorization of a positive integer >= 2.
# The code is fast only for integers 5 digits or fewer.
# Example (Ubuntu terminal):
# python2 prime_factors.py
# Enter integer: 56225
# [5, 5, 13, 173]
n = int(raw_input("Enter integer: "))
import math 
count = 1
primes = [2]
for i in range(2,n+1):
    val = True
    for j in range(2,int(math.floor(math.sqrt(i)))+1):
        if i % j == 0:
            val = False
    if val:
        primes.append(i)
factors = []
while n>1:
    for p in primes:
    	while n%p == 0:
            n /= p
            factors.append(p)

print factors
