"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 2

    for i in range(num, number_of_primes):
        for j in range(num, i):
            if i%j == 0:
                break
            else:
                list.append(i)
    return list
