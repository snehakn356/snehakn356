def fibonacci(n):
    fib_series = [0, 1]
    for _ in range(n - 2):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]


N = int(input("Enter the number of Fibonacci numbers: "))
print(f"First {N} Fibonacci numbers:", fibonacci(N))

print("Sneha EC067")
