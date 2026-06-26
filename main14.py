a = 5
b = 10

print("--- TASK 1: XOR SWAP ---")
print("Before swapping:")
print("a =", a)
print("b =", b)

a = a ^ b
b = a ^ b  
a = a ^ b 

print("After swapping:")
print("a =", a)
print("b =", b)
print()  


number_to_double = 7

print("--- TASK 2: LEFT SHIFT DOUBLING ---")
doubled_result = number_to_double << 1
print("Original number:", number_to_double)
print("Doubled number using left shift:", doubled_result)
print()


x = 4
y = -5

print("--- TASK 3: SIGN DETECTION WITH XOR ---")
print("Checking numbers:", x, "and", y)

if (x ^ y) < 0:
    print("Result: Yes, the numbers have different signs!")
else:
    print("Result: No, the numbers have the same sign.")
print()


number_to_divide = 45

print("--- TASK 4: RIGHT SHIFT DIVISION ---")
divided_result = number_to_divide >> 1
print("Original number:", number_to_divide)
print("Divided by 2 using right shift:", divided_result)