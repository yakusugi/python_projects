import subprocess

# Define the commands to be run
commands = ["ls -l", "df -h", "uname -a"]

# Iterate through the commands
for command in commands:
    # Run the command and capture the output
    output = subprocess.run(command, shell=True, capture_output=True)

    # Print the output
    print(output.stdout.decode())
