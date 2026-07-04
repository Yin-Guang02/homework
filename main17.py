# ================================
# MY COUNTDOWN TIMER CHALLENGE
# ================================
# Topics:
# What Is Recursion? | Base Case | Build and Unwind
# Counting with Recursion | Factorial Using Recursion | Stack Overflow

print("================================")
print("MY COUNTDOWN TIMER CHALLENGE")
print("================================")


# ------------------------------------------------
# PART 1 — WHAT IS RECURSION?
# ------------------------------------------------
# Recursion means a function calls itself.
# A recursive function must have:
# 1. A base case to stop
# 2. A recursive call with a smaller problem


# ------------------------------------------------
# PART 2 — COUNTDOWN WITH RECURSION
# ------------------------------------------------

def countdown(number):
    # Base Case
    if number == 0:
        print("Time is up!")
        return

    print(number)
    countdown(number - 1)


print("\nCountdown from 5:")
countdown(5)


# ------------------------------------------------
# PART 3 — HOW RECURSION BUILDS AND UNWINDS
# ------------------------------------------------

def build_and_unwind(level):
    # Base Case
    if level == 0:
        print("Base case reached. Now unwinding begins.")
        return

    print("Building level:", level)
    build_and_unwind(level - 1)
    print("Unwinding level:", level)


print("\nBuild and Unwind Demo:")
build_and_unwind(3)


# ------------------------------------------------
# PART 4 — COUNTING WITH RECURSION
# ------------------------------------------------

def count_up(number):
    # Base Case
    if number > 10:
        return

    print(number)
    count_up(number + 1)


print("\nCounting from 1 to 10:")
count_up(1)


# ------------------------------------------------
# PART 5 — FACTORIAL USING RECURSION
# ------------------------------------------------

def factorial(number):
    # Base Case
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print("\nFactorial Result:")
print("5! =", factorial(5))


# ------------------------------------------------
# PART 6 — STACK OVERFLOW SAFETY DEMO (FIXED)
# ------------------------------------------------

def safe_countdown(number):
    # FIXED: Added a base case to prevent stack overflow
    if number < 0:
        print("Blast off! (Safely stopped)")
        return
        
    print(number)
    # FIXED: The recursive call is now safe to execute
    safe_countdown(number - 1)


print("\nSafe Countdown Demo:")
print("Running the corrected recursive function:")
safe_countdown(3)
print("================================")