def is_palindrome(s):
    # Step 1: Normalize the string
    normalized_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Step 2: Check if the normalized string is equal to its reverse
    return normalized_s == normalized_s[::-1]

# Example usage:
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("race a car"))  # Output: False
print(is_palindrome(" "))  # Output: True
# -----------------------

def is_palindrome(s):
    # Step 1: Normalize the string
    normalized_s = ""
    for char in s:
        if char.isalnum():  # Check if the character is alphanumeric
            normalized_s += char.lower()  # Convert to lowercase and add to the normalized string
    
    # Step 2: Check if the normalized string is equal to its reverse
    return normalized_s == normalized_s[::-1]

# Example usage:
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("race a car"))  # Output: False
print(is_palindrome(" "))  # Output: True
