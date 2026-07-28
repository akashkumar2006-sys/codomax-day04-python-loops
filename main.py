# ==========================================
# Codomax AI/ML Internship - Day 4
# Topic: Loops in Python
# Author: Akash Kumar Jha
# ==========================================

print("=" * 55)
print("          PYTHON LOOPS - DAY 4")
print("=" * 55)

# Print numbers from 1 to 10
print("\n1. Numbers from 1 to 10")

for i in range(1, 11):
    print(i, end=" ")

print("\n")

# Multiplication Table
num = int(input("2. Enter a number for multiplication table: "))

print("\nMultiplication Table\n")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Sum of first N natural numbers
n = int(input("\n3. Enter value of N: "))

sum_num = 0

for i in range(1, n + 1):
    sum_num += i

print("Sum =", sum_num)

# Factorial

fact = 1

number = int(input("\n4. Enter a number to find factorial: "))

for i in range(1, number + 1):
    fact *= i

print("Factorial =", fact)

# Star Pattern

print("\n5. Star Pattern\n")

for i in range(1, 6):
    print("*" * i)

print("\nProgram Executed Successfully ✅")
print("=" * 55)
