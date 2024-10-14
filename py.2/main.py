# Solve the problem from the second set here
# The palindrome of a number is the number obtained by reversing the order of its digits(273=372).For a given natural number
#determine its palindrome
n = int(input("Enter a number:"))
palindrom= 0

while n > 1:
        palindrom = palindrom * 10 + int(n % 10) #here we determine the palindrom by the formula
        n = int(n / 10)

print(palindrom)
