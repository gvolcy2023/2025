from netmiko import ConnectHandler

# Define Cisco switch credentials and parameters
device = {
    "device_type": "cisco_ios",
    "ip": "10.1.11.250",
    "username": "admin",
    "password": "cisco",
}

# BGP configuration commands
bgp_config = [
    "router bgp 65001",
    "bgp log-neighbor-changes",
    "neighbor 10.1.11.1 remote-as 65002",
    "network 192.168.1.0 mask 255.255.255.0"
]

# Connect and push configuration
try:
    connection = ConnectHandler(**device)
    output = connection.send_config_set(bgp_config)
    print("BGP Configuration Sent:\n")
    print(output)
    connection.disconnect()
except Exception as e:
    print(f"Error: {e}")
