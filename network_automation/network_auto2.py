import subprocess

hostname = "192.168.0.104" # replace with the hostname or IP address of the server you want to ping
response = subprocess.run(["ping", "-c", "1", hostname], capture_output=True, text=True)

if "1 packets transmitted, 1 received" in response.stdout:
    print(f"{hostname} is online.")
else:
    print(f"{hostname} is offline.")