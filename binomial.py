# runs as is for python 2.7 interpreter.

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

