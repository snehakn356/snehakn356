def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("madam"))       
print(is_palindrome("hello"))       
print(is_palindrome("Racecar"))  
