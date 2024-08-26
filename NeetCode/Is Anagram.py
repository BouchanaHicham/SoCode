# ------------------------------------------------------------------

# Approach 1: Sorting
def is_anagram_sorting(s, t):
    # If the lengths are not the same, they can't be anagrams
    if len(s) != len(t):
        return False
    # Sort both strings and compare them
    return sorted(s) == sorted(t)

# ------------------------------------------------------------------

# Approach 2: Using a Dictionary (Hash Map)
def is_anagram_hash_map(s, t):
    # If the lengths are not the same, they can't be anagrams
    if len(s) != len(t):
        return False
    
    # Create a dictionary to count occurrences of each character
    char_count = {}
    
    # Count each character in the first string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrease the count for each character in the second string
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    # If all counts are zero, they are anagrams
    return all(count == 0 for count in char_count.values())

# ------------------------------------------------------------------

# Approach 3: Character Count Array
def is_anagram_char_count(s, t):
    # If the lengths are not the same, they can't be anagrams
    if len(s) != len(t):
        return False
    
    # Create an array of 26 zeroes (assuming only lowercase letters)
    count = [0] * 26
    
    # Increment and decrement the count based on the characters in the strings
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    
    # If all counts are zero, they are anagrams
    return all(x == 0 for x in count)

# ------------------------------------------------------------------
