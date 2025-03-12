def sum_of_evens(start, end):
    return sum(i for i in range(start, end + 1) if i % 2 == 0)

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print("Sum of even numbers:", sum_of_evens(start, end))
