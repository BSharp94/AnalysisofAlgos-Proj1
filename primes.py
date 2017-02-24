
#
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def prime_factor(n):
    primes = get_primes(n)

print "value {} with primes {}".format(45,get_primes(45))






