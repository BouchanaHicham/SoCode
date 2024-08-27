def roman_to_int(s):
    # Create a mapping of Roman numerals to their integer values.
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # print(str(reversed(s)))
    # Iterate through the string in reverse order
    revS = reversed(s)
    for char in revS: 
        current_value = roman_values[char]
        # If the current value is less than the previous value, subtract it
        if current_value < prev_value:
            total -= current_value
        else:
            # Otherwise, add it to the total
            total += current_value

        prev_value = current_value
    
    return total

# Example usage:
print(roman_to_int("III"))    # Output: 3
print(roman_to_int("IV"))     # Output: 4
print(roman_to_int("IX"))     # Output: 9
print(roman_to_int("LVIII"))  # Output: 58
print(roman_to_int("MCMXCIV")) # Output: 1994
