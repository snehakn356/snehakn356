def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)
print(find_lcm(12, 18))  
