import itertools as iter
import math
setA={'1','5','76','12'}
setB={'5','2','65','2'}
setA-setB
setA|setB
setA&setB
iter.permutations(setA)

for x in iter.permutations(setA):
    print(x)


def factorial(n):
    if n is 0:
        return 1
    return n * factorial(n-1)

print(factorial(2))

def factors(n):
    res = set()
    for x in range(1,math.floor(n/2)+1):
        if n%x is 0:
            res.add(x)
    res.add(n)
    return res

print(factors(4))
print(factors(6))

for x in iter.combinations(factors(6),2):
    print(x)


def gcd(a,b):
    factA = factors(a)
    factB = factors(b)
    return max(factA.intersection(factB))


def prove_pi():
    return math.pi

print(prove_pi())
gcd(4,6)
gcd(12,48)
