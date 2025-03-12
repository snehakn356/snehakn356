numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))


squared_numbers = list(map(lambda x: x ** 2, numbers))

print("Even numbers:", even_numbers)
print("Squared numbers:", squared_numbers)
