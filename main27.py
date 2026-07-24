binary_input = input("Enter your Binary: ")

decimal_value = 0
power = 0

for bit in reversed(binary_input):
    if bit == '1':
        decimal_value += 2 ** power
    power += 1

print("Decimal :", decimal_value)