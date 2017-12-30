# Runs as is for python 2.7 interpreter.
def prime_list(n):
    """
    prime_factors(n) prints the prime factorization of a positive integer >= 2.
    The code is fast only for integers 5 digits or fewer.
    
    Example (Ubuntu terminal):
    $ python2 prime_factors.py
    Enter integer: 89556
    [2, 2, 3, 17, 439]
    """
    if n <= 1:
        pass
    else:
        primes = range(2,n/2+1)
        i = 0
        j = 2
        while primes[i]*j in primes:
            while primes[i]*j in primes:
                primes.remove(primes[i]*j)
                j += 1
            else:
            	i += 1
        	j = primes[i]
        	continue
        factors = []
        while n>1:
            for p in primes:
            	while n%p == 0:
                    n /= p
                    factors.append(p)
        return factors

n = int(raw_input("Enter integer: "))
factors = prime_list(n)
print factors
