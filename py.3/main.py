# Solve the problem from the third set here
# Generate the largest perfect number smaller than a given natural number n. If such a number does not exist, a message should be displayed. A number is perfect if it is equal to the sum of its divisors, except itself. (e.g. 6 is a perfect number, as 6=1+2+3).
from math import sqrt
n = int(input("Enter a number:"))       #Enter a number
n= n - 1
def Verify_Perfect_Number(n):           #verifies if the number is a perfect one
    s = 0
    for i in range (1, int((n/2)+1)):
        if n % i == 0:
            s = s + i
    if s == n: return True

def Number_decrease(n):            #keeps decresing the number until it finds a perfect number,if not it shows the message
    if Verify_Perfect_Number(n): print(n)
    elif n > 1:
        n = n-1
        Number_decrease(n)
    else: print("Such a number doesn't exist")


Number_decrease(n)
