def is_palindrome(value):
    return str(value) == str(value)[::-1]

data = input("Enter a number or string: ")
print("Palindrome" if is_palindrome(data) else "Not a palindrome")
