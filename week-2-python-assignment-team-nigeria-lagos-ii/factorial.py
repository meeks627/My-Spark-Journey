# Factorial of a Number (Recursion)
# Filename: factorial.py
# Write a recursive function `factorial(n)` to compute the factorial of a given number n.

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else: 
        return n * factorial(n - 1)
    # Implement function