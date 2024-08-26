def contains_duplicate(nums):
    # Outer loop: iterate over each element in the array
    for i in range(len(nums)):
        # Inner loop: compare the current element with every other element
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True  # Duplicate found
    return False  # No duplicates found

# ------------------------------------------------

def contains_duplicate(nums):
    seen = set()  # Initialize an empty set to store seen numbers
    for num in nums:
        if num in seen:
            return True  # Duplicate found
        seen.add(num)  # Add the number to the set
    return False  # No duplicates found

# ------------------------------------------------------------------

def contains_duplicate(nums):
    # Sort the array
    nums.sort()
    
    # Check for consecutive duplicates
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True  # Duplicate found
    return False  # No duplicates found

# ------------------------------------------------------------------

