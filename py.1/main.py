# Solve the problem from the first set here
# Generate the first prime number larger than a given natural number n.
from math import sqrt
def prime_number(n):        # The prime_nunmber fucntion checks if the number is a prime number
    if n < 2: return False
    if n == 2: return True
    for i in range (2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True

def next_number(n): #if the number is not a prime number it goes to the next numberc,if the number is prime it prints it
    if prime_number(n):
        print(n)
    else:
        n+=1
        next_number(n)

n = int(input("Enter a number: "))
next_number(n)