from math import sqrt

def inchesToCM(inches):
    return int(round(inches * 2.54))

assert 91 == inchesToCM(36)
# 91.0 DNE 91 (:
assert type(inchesToCM(36)) is int

def getFactors(n):
    if n < 1:
        raise Exception("no")

    factors = list()
    for left in range(1, int(sqrt(n))+1):
        if n % left == 0:
            right = n / left
            factors.append(left)
            if left != right:
                factors.append(right)

    return sorted(factors)


assert getFactors(1) == [1]
assert getFactors(25) == [1, 5, 25]
assert getFactors(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36]
assert getFactors(100) == sorted([1, 100, 2, 50, 4, 25, 5, 20, 10])


for i in range(2, 100000):
    if i % 10000 == 0:
        print("processing {}".format(i))

    factors=getFactors(i)
    sumFactors=sum(factors)
    iInCM=inchesToCM(i)

    if sumFactors == iInCM:
        print(i, iInCM, factors)
