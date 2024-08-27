def reverse_string(s):
    left  = 0
    right = len(s) - 1
    while left < right:
        s[left]  = s[right]
        s[right] = s[left]
        left += 1
        right -= 1
    return s


def reverse_string_ez(s):
    return s[::-1]

# Example usage:
s = ["h","e","l","l","o"]
print(reverse_string(s))  # Output: ["o","l","l","e","h"]
