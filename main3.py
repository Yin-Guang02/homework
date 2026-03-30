def fibonacci_recursive(n):
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:  
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
terms = int(input("How many Fibonacci terms would you like to print? "))
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for i in range(terms):
        print(fibonacci_recursive(i), end=" ")