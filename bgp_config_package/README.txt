This Python script uses Netmiko to SSH into a Cisco Catalyst switch or router and configure BGP.

Steps:
1. Connects via SSH to the IP (edit in the script).
2. Logs in with specified credentials.
3. Applies basic BGP configuration:
   - Sets the local ASN to 65001
   - Configures a neighbor (10.1.11.1) with ASN 65002
   - Advertises network 192.168.1.0/24
4. Prints the device response.

Edit IP, username, password, and BGP details as needed.
