def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

n = int(input("Enter N: "))
print("Sum of squares:", sum_of_squares(n))
