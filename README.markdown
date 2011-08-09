# Python Cisco Switch SNMP Monitoring for Spanning-tree
This small script outputs a list of active VLANs, the ports associated with them and their STP port status: disabled, blocking, forwarding, and so forth. It might be used to monitor Spanning-tree.
## How it works
The script polls for the active VLANs on the switch. It then retrieves STP port status by VLAN.
## How to use
Simply change the IP address, port and username of your switch's SNMP service. You can easily adapt the script for automation over multiple devices. Please refer to the pySNMP documentation for more advanced SNMP development.
## Support
Feel free to send me an email at lussier at the IEEE organization domain name.
