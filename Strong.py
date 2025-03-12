def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    return n == sum(int(digit) ** num_len for digit in num_str)

num = int(input("Enter a number: "))
print("Armstrong Number" if is_armstrong(num) else "Not an Armstrong Number")
