# runs as is for python 2.7 interpreter.
# prints out the binomial coefficients for (x+y)^n, where n is a nonnegative integer.
# Example (Ubuntu terminal):
# python2 binomial.py
# Enter exponent: 11
# [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1]
def factorial(n):
    if n == 0:
        return 1
    else:
        f = 1
        for i in xrange(1,n+1):
            f = f*i
        return f

n = int(raw_input("Enter exponent: "))
coeffs = []
nfac = factorial(n)
for j in range(0,n+1):
    coeffs.append(nfac/(factorial(j)*factorial(n-j)))
print coeffs
