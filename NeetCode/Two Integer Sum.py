# ------------------------------------------------------------------

# Approach 1: Brute Force
def two_sum_brute_force(nums, target):
    # Outer loop: iterate over each element in the array
    for i in range(len(nums)):
        # Inner loop: compare the current element with every other element
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j  # Return the indices if the sum matches the target
    return None  # Return None if no such pair is found

# ------------------------------------------------------------------

# Approach 2: Using a Dictionary (Hash Map)
def two_sum_hash_map(nums, target):
    # Dictionary to store the index of the numbers we've seen
    prevMap = {}
    
    for i, num in enumerate(nums):
        diff  = target - num
        if diff  in prevMap:
            return prevMap[diff ], i  # Return the indices if the diff  is found
        prevMap[num] = i  # Store the index of the current number
    return None  # Return None if no such pair is found

# ------------------------------------------------------------------

# Approach 3: Two-Pointer Technique (for sorted arrays)
def two_sum_two_pointers(nums, target):
    # Sort the array while keeping track of the original indices
    nums_with_indices = sorted(enumerate(nums), key=lambda x: x[1])
    
    left, right = 0, len(nums_with_indices) - 1
    
    while left < right:
        current_sum = nums_with_indices[left][1] + nums_with_indices[right][1]
        if current_sum == target:
            return nums_with_indices[left][0], nums_with_indices[right][0]  # Return the original indices
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None  # Return None if no such pair is found
