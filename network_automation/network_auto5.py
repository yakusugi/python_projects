import subprocess
import sys

if len(sys.argv) < 2:
    print("Please specify a file containing the list of servers.")
    sys.exit(1)

filename = sys.argv[1]
try:
    with open(filename, "r") as f:
        servers = f.read().splitlines()
except FileNotFoundError:
    print(f"Error: The file {filename} could not be found.")
    sys.exit(1)

for hostname in servers:
    response = subprocess.run(["ping", "-c", "1", hostname], capture_output=True, text=True)

    if "1 packets transmitted, 1 received" in response.stdout:
        print(f"{hostname} is online.")
    else:
        print(f"{hostname} is offline.")
