a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b:
    if a >= c:
        max_num = a
    else:
        max_num = c
else:
    if b >= c:
        max_num = b
    else:
        max_num = c

print(f"Largest number: {max_num}")
