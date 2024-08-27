# . Reverse a List
# Problem: Write a function that takes a list and returns it in reverse order without using slicing ([::-1]).
# Example:
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

def reverse_list(lst):
    # Initialize pointers
    left = 0
    right = len(lst) - 1
    
    # Swap elements from both ends towards the center
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    
    return lst

# Example usage:
print(reverse_list([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]
