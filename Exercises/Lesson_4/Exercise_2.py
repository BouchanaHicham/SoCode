# Write a program that writes a list of names to a file, then reads and displays the content of that file.

# Solution
def write_names_to_file(filename, names):
    with open(filename, "w") as file:
        for name in names:
            file.write(name + "\n")

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# List of names
names_list = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# Write the names to the file
write_names_to_file("names.txt", names_list)

# Read and display the content of the file
read_file("names.txt")
