import os

ip_list = ["192.168.0.104", "192.168.0.104", "192.168.0.105"]

for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Recieved = 4" in response:
        print(f"UP {ip} Ping successful")
    else:
        print(f"DOWN {ip} Ping unsuccessful")