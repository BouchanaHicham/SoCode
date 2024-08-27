def is_palindrome(x):
    str_x = str(x)
    return str_x == str_x[::-1]

# ----------------------------------

def is_palindrome(s):
    # Convert the input to a string (if not already)
    str_s = str(s)
    
    # Initialize two pointers
    left = 0
    right = len(str_s) - 1
    
    # Compare characters from both ends moving towards the center
    while left < right:
        if str_s[left] != str_s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Example usage:
print(is_palindrome("121"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("madam"))  # Output: True