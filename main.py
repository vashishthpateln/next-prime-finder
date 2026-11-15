"""
Provide a script that computes, then prints the first prime number greater than the provided number.
"""

import itertools

def is_prime(n):
    number_list = [i for i in range(2, int(n**0.5)+1)] # Only need to check up to the square root of n because if n is divisible by any number greater than its square root, it must also be divisible by a number smaller than its square root.
    if n < 2:
        return False
    if n == 2:
        return True
    for number in number_list:
        if n % number == 0:
            return False
    return True

def generator(n): # It is easier to check many smaller functions than one big function
    for i in itertools.count(n+1):
        if is_prime(i):
            return i


user_input = int(input("Enter a number to find the next prime number greater than it: "))
print(generator(user_input))