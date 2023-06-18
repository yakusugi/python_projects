import sys

# Check if the number of arguments is correct
if len(sys.argv) != 2:
    print("Usage: cat.py <file>")
    sys.exit(1)

# Open the file
try:
    with open(sys.argv[1], 'r') as file:
        # Read and print the contents of the file
        print(file.read())
except FileNotFoundError:
    print(f"Error: Unable to open file {sys.argv[1]}")
    sys.exit(1)
