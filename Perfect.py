def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

num = int(input("Enter a number: "))
print("Perfect Number" if is_perfect(num) else "Not a Perfect Number")
