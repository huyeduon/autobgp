# autobgp
BGP peering auto-reconfiguration on ACI leaf. </br>
At stead state LA1 and LA2 are in VPC pair, however only one of the node has BGP peering to external device. For example LA1 has peering to external device. 
If LA1 is down or reload, BGP peering will be auto-reconfigured to LA2. 
If LA1 comes back, BGP peering will not change. There is no pre-empt. </br>
config.py includes site information such as apic ip address/username/password.

