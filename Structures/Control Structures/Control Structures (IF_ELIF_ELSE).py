
# Ask the user for their age
age = int(input("Please enter your age: "))

# Determine the age category and display a message
if age < 18:
    print("You are a minor.")
elif age >= 18 and age <= 65:
    print("You are an adult.")
else:
    print("You are a senior.")