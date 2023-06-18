import subprocess

with open("hostname_list.txt", "r") as f:
    servers = f.read().splitlines()

for hostname in servers:
    response = subprocess.run(["ping", "-c", "1", hostname], capture_output=True, text=True)

    if "1 packets transmitted, 1 received" in response.stdout:
        print(f"{hostname} is online.")
    else:
        print(f"{hostname} is offline.")