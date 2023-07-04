# autobgp
BGP peering auto-reconfiguration on ACI leaf. </br>
At stead state LA1 and LA2 are in VPC pair, however only one of the node has BGP peering to external device. For example LA1 has peering to external device. 
If LA1 is down or reload, BGP peering will be auto-reconfigured to LA2. 
If LA1 comes back, BGP peering will not change. There is no preemption. </br>
The script is confined to a pair of leaf with one L3Out, it can be extended to support multiple pair of leaf and multiple L3out in multisites.</br></br>
config.py includes site information such as apic ip address/username/password.</br>

To test script:</br>
python3 autobgp.py </br>
What the console to see which Leaf is active and its BGP peering state.</br>
Reload or shutdown the leaf who has BGP peering state established will trigger BGP reconfiguration to the other leaf.</br>

