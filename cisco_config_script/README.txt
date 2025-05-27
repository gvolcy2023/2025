Cisco Automation Script
=======================

This script connects to a Cisco IOS device via SSH and applies a standard configuration:
- VLAN 10
- IP address: 10.10.10.10 255.55.255.0
- SNMP settings
- NTP server
- AAA configuration
- ACL for VTY access

Usage:
1. Make sure you have `netmiko` installed: pip install netmiko
2. Run the script: python configure_cisco.py
3. Enter IP, username, and passwords when prompted

Author: ChatGPT
