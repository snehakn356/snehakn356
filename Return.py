def reverse_number(n):
    return int(str(n)[::-1])

num = int(input("Enter an integer: "))
print("Reversed:", reverse_number(num))
