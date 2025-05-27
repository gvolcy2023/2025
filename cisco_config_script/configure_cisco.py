from netmiko import ConnectHandler
import getpass

# Cisco device details
device = {
    "device_type": "cisco_ios",
    "ip": input("Enter device IP: "),
    "username": input("Enter SSH username: "),
    "password": getpass.getpass("Enter SSH password: "),
    "secret": getpass.getpass("Enter enable secret: "),
}

# Configuration commands
config_commands = [
    "vlan 10",
    "name DATA_VLAN",
    "interface vlan 10",
    "ip address 10.10.10.10 255.55.255.0",
    "no shutdown",
    "exit",
    "snmp-server community public RO",
    "snmp-server location LAB",
    "snmp-server contact admin@example.com",
    "ntp server 192.168.1.1",
    "aaa new-model",
    "aaa authentication login default local",
    "aaa authorization exec default local",
    "username admin privilege 15 secret admin123",
    "ip access-list standard MGMT-ACL",
    "permit 10.0.0.0 0.255.255.255",
    "deny any",
    "line vty 0 4",
    "access-class MGMT-ACL in",
    "login local",
    "transport input ssh",
]

def main():
    try:
        print("\nConnecting to device...")
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        print("Connected. Sending configuration...")
        output = net_connect.send_config_set(config_commands)
        print(output)
        net_connect.save_config()
        print("Configuration saved.")
        net_connect.disconnect()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
