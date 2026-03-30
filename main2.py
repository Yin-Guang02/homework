num_str = input("Enter a number to check: ")
num = int(num_str)

order = len(num_str)

sum_of_powers = 0
temp = num

while temp > 0:
    digit = temp % 10            
    sum_of_powers += digit ** order  
    temp //= 10                 

if num == sum_of_powers:
    print(f"{num} is an Armstrong Number!")
else:
    print(f"{num} is NOT an Armstrong Number.")
