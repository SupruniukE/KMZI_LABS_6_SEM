import math

def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b

def nod3(a, b, c):
    return nod(nod(a, b), c)

def primes(n, m):
    count = 0
    print(f"Primes from {n} to {m}:")
    for num in range(n, m+1):
        n = 0
        for n in range(2, num):
            if num % n == 0:
                break
        if num == 2:
            print(num)
        if n == num - 1:
            count += 1
            print(num)
    return count

print("NOD(379,411) =", nod(379, 411))
print("NOD(12, 24, 3) =", nod3(12, 24, 3))
print("Count primes =", primes(2, 411))
print(411/math.log(411, math.e))