def count_digits(n):
    return len(str(abs(n)))

num = int(input("Enter an integer: "))
print("Number of digits:", count_digits(num))
