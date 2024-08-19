# Write a program that reads the content of a file and displays it on the screen.

# Solution

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# Call the function
read_file("example.txt")
