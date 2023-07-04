# autobgp
BGP peering auto-reconfiguration on ACI leaf. </br>
At steady state LA1 and LA2 are in VPC pair, however only one of the node has BGP peering to external device. For example LA1 has peering to external device. 
If LA1 is down or reload, BGP peering will be auto-reconfigured to LA2. 
If LA1 comes back, BGP peering will not change. There is no preemption. </br>
The script is confined to a pair of leaf with one L3Out, it can be extended to support multiple pair of leaf and multiple L3out in multisites.</br></br>
The config.py includes site information such as apic ip address/username/password.</br>
The script runs based on pull model where it keeps monitoring BGP state and fabric node state (active or not active)</br>


## To test script:</br>
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
The script can be expanded to multiple border leaf, l3outs and sites. We can think about multiple thread to support continous monitoring and reconfigure multiple objects at same the time.</br>
Combination of both pull and push model, that would require event subscription and more complicated logic, however the outcome will better and more responsive.</br>