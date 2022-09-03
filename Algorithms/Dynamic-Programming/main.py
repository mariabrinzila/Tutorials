import fibonacci as fib
import factorial as fact
import ugly_numbers as ugly


# Fibonacci (tabulation)
n = 11

print("The " + str(n) + "-th element in the Fibonacci sequence is: "
      + str(fib.fibonacci_tabulation(n)) + " (tabulation)")

# Fibonacci (memorization)
n = 8
lookup = [None] * (n + 1)

print("The " + str(n) + "-th element in the Fibonacci sequence is: "
      + str(fib.fibonacci_memorization(n, lookup)) + " (memorization)")
print("---------------------------------------")

# Factorial (tabulation)
n = 5

print("The result of " + str(n) + "! is: " + str(fact.factorial_tabulation(n)) + " (tabulation)")

# Factorial (memorization)
n = 10
lookup = [None] * (n + 1)

print("The result of " + str(n) + "! is: " + str(fact.factorial_memorization(n, lookup))
      + " (memorization)")
print("---------------------------------------")

# Ugly numbers
n = 150

print("The " + str(n) + "-th ugly number is: " + str(ugly.ugly_numbers_memorization(n)))
print("---------------------------------------")
