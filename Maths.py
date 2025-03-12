import math

def math_operations(n):
    return {
        "Square Root": math.sqrt(n),
        "Factorial": math.factorial(n),
        "Sine": math.sin(math.radians(n))  
    }
print(math_operations(5))
