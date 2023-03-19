from sys import argv
import time as t
import gpu

def is_prime(n):
    factors = 0
    for i in range(2, n):
        if n % i == 0:
            factors += 1
    return factors == 0

limit = int(argv[1])
total = 0

start = t.time()
@par(gpu=True)
for i in range(2, limit):
    if is_prime(i):
        total += 1
time = t.time() - start
print('Found %d primes in %f seconds' % (total, time))