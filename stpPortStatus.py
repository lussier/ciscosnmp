from pysnmp.entity.rfc3413.oneliner import cmdgen

#################################################################################################
# Global Settings
deviceIPAddress = "192.168.254.250"
snmpPort = 161
snmpUsername = "public"
# Port Status Displayed Information
statusID = {1:"Disabled", 2:"Blocking", 3:"Listening", 4:"Learning", 5:"Forwarding", 6:"Broken"}
#################################################################################################

# Retrieve VLAN Table
errorIndication, errorStatus, errorIndex, varBinds = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('agent',snmpUsername,0),cmdgen.UdpTransportTarget((deviceIPAddress,snmpPort)),(1,3,6,1,4,1,9,9,46,1,3,1,1,2))
# Store VLAN Table
vlans = []
for row in varBinds:
    for item in row:
        vlans.append(item[0][15])
# Retrieve STP port status information
vlanAndSTP = {}
for vlan in vlans:
    username = '%s@%s' % (snmpUsername,vlan)
    errorIndication, errorStatus, errorIndex, varBinds = cmdgen.CommandGenerator().nextCmd(cmdgen.CommunityData('agent',username,0),cmdgen.UdpTransportTarget((deviceIPAddress,snmpPort)),(1,3,6,1,2,1,17,2,15,1,3))
# Store STP port status information
    stpPortInfoForThisVLAN = {}
    for row in varBinds:
        for item in row:
            port    = item[0][11]
            status  = item[1]
            stpPortInfoForThisVLAN[port] = status
    vlanAndSTP[vlan] = stpPortInfoForThisVLAN
# Display final dictionary
for item in vlanAndSTP.iteritems():
    if item[1]:
        for subitem in item[1].iteritems():
            vlanID = str(item[0])
            portNumber = str(subitem[0])
            portStatusID = subitem[1]
            portStatusDescription = statusID[portStatusID]
            vlanStr = "VLAN " + vlanID
            space1 =  " "*(15-len(vlanStr))
            portStr = "PORT " + portNumber
            space2 = " "*(15-len(portStr))
            print vlanStr + space1 + portStr + space2 + portStatusDescription
