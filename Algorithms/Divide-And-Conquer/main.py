import power as p
import towers_of_Hanoi as th


# Power (x to the n-th power)
x = 3
n = 10

print(str(x) + " to the " + str(n) + "-th power is: " + str(p.power(x, n)))
print("---------------------------------------")

# Towers of Hanoi
# The overall number of moves to solve the problem is 2 ^ n - 1
n = 4

th.towers_hanoi(n, 'R1', 'R2', 'R3')
