import subprocess
import sys

if len(sys.argv) < 3:
    print("Please specify a file containing the list of servers and a file to write the results.")
    sys.exit(1)

servers_file = sys.argv[1]
results_file = sys.argv[2]

try:
    with open(servers_file, "r") as f:
        servers = f.read().splitlines()
except FileNotFoundError:
    print(f"Error: The file {servers_file} could not be found.")
    sys.exit(1)

results = []
for hostname in servers:
    response = subprocess.run(["ping", "-c", "1", hostname], capture_output=True, text=True)

    if "1 packets transmitted, 1 received" in response.stdout:
        results.append(f"{hostname} is online.")
    else:
        results.append(f"{hostname} is offline.")

try:
    with open(results_file, "w") as f:
        for result in results:
            f.write(result + "\n")
    print(f"Results written to {results_file}.")
except FileNotFoundError:
    print(f"Error: The file {results_file} could not be found.")
    sys.exit(1)