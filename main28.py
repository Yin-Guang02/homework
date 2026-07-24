num1 = int(input("Enter Largest number : "))
num2 = int(input("Enter Smallest number : "))

a = num1
b = num2

while b != 0:
    a, b = b, a % b

gcd = a

lcm = (num1 * num2) // gcd

print("LCM is :", lcm)