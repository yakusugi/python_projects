import subprocess

servers = ["192.168.0.104", "192.168.0.107", "192.168.0.105"]

for hostname in servers:
    response = subprocess.run(["ping", "-c", "1", hostname], capture_output=True, text=True)

    if "1 packets transmitted, 1 received" in response.stdout:
        print(f"{hostname} is online.")
    else:
        print(f"{hostname} is offline.")
