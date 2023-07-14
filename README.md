# autobgp
The script aims to automate BGP peering reconfiguration on ACI leaf switches. In the steady state, LA1 and LA2 operate as a VPC pair, with only one of the nodes having BGP peering established with an external device. For instance, if LA1 is the active peering node and experiences downtime or undergoes a reload, the script will automatically reconfigure the BGP peering to LA2. However, if LA1 comes back online, the BGP peering will remain unchanged, as there is no preemption mechanism in place.</br>

The current implementation of the script is designed for a specific scenario involving a pair of leaf switches with a single L3Out. However, it can be extended to support multiple pairs of leaf switches and multiple L3Outs across multiple sites in a multisite deployment.</br>

The configuration details, such as the APIC IP address, username, and password, are stored in the config.py file. The script operates on a pull model, continuously monitoring the BGP state and fabric node state (active or not active). It periodically checks the status of the BGP peering and the overall health of the leaf switches.</br>

By employing this approach, the script ensures that the BGP peering remains functional and automatically switches to the backup leaf switch when necessary, without requiring manual intervention. This enhances the stability and reliability of the BGP peering infrastructure in the ACI fabric.</br>


## How to test script:</br>
python3 autobgp.py </br>
Watch the console to see which Leaf is active and its BGP peering state.</br>
Reload or shutdown the leaf who has BGP peering state established will trigger BGP reconfiguration to the other leaf.</br>
## Setup and state info </br>
SideA: </br>
LA1: Bordler Leaf node ID 1201 </br></br>

SideB:</br>
LA2: Border Leaf node ID 1202 </br></br>

Sample state info:</br>

LA1 fabric Node state:  active</br>
LA2 fabric Node state:  active</br>
LA1 BGP peering state: idle</br>
SideA configured state: False</br>
-------------******---------------</br>
LA2 BGP peering state: established</br>
SideB configured state: True</br>
-------------******---------------</br>
LA1 fabric Node state:  active</br>
LA2 fabric Node state:  active</br>
LA1 BGP peering state: idle</br>
SideA configured state: False</br>
-------------******---------------</br>


## What's next</br>
The script can be enhanced to support multiple border leafs, L3Outs, and sites, enabling scalability. You can utilize data structures like lists or dictionaries to store object information, such as APIC URLs, credentials, and identifiers. By iterating through these structures, you can perform operations on each object individually.


## Update</br>
The script has been involved to support multiple sites, multiple border leafs, l3outs </br>
To run the script: </br>

python fullautobgp.py