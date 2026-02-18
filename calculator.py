import sys

if len(sys.argv) < 3:
    print("Provide two numbers")
    sys.exit(1)

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
