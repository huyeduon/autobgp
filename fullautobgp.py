# Author: Huyen Duong, CNBU TME, Cisco Systems
# Quality: POC level
import requests
import json
import time
import threading
import re
requests.packages.urllib3.disable_warnings()
from config import s1apic, s1user, s1password, s2apic, s2user, s2password
from config import LA1_bgp_url, LA2_bgp_url, LA3_bgp_url, LA4_bgp_url, LB1_bgp_url, LB2_bgp_url
from config import rsPath_LA12_tenant5_v307_v4, rsPath_LA12_tenant5_v307_v6, rsPath_LA12_tenant6_v513_v4, rsPath_LA12_tenant6_v513_v6, rsPath_LA12_tenant6_v704_v4, rsPath_LA12_tenant6_v704_v6
from config import rsPath_LA34_tenant5_v308_v4, rsPath_LA34_tenant5_v308_v6, rsPath_LA34_tenant6_v515_v4, rsPath_LA34_tenant6_v515_v6, rsPath_LA34_tenant6_v708_v4, rsPath_LA34_tenant6_v708_v6
from config import rsPath_LB12_tenant6_v514_v4, rsPath_LB12_tenant6_v514_v6, rsPath_LB12_tenant6_v516_v4, rsPath_LB12_tenant6_v516_v6, rsPath_LB12_tenant6_v712_v4, rsPath_LB12_tenant6_v712_v6
from config import rsPath_LA12_tenant5_v307_v4_LocA, rsPath_LA12_tenant5_v307_v4_LocB, rsPath_LA12_tenant5_v307_v6_LocA, rsPath_LA12_tenant5_v307_v6_LocB
from config import rsPath_LA12_tenant6_v513_v4_LocA, rsPath_LA12_tenant6_v513_v4_LocB, rsPath_LA12_tenant6_v513_v6_LocA, rsPath_LA12_tenant6_v513_v6_LocB
from config import rsPath_LA12_tenant6_v704_v4_LocA, rsPath_LA12_tenant6_v704_v4_LocB, rsPath_LA12_tenant6_v704_v6_LocA, rsPath_LA12_tenant6_v704_v6_LocB
from config import rsPath_LA34_tenant5_v308_v4_LocA, rsPath_LA34_tenant5_v308_v4_LocB, rsPath_LA34_tenant5_v308_v6_LocA, rsPath_LA34_tenant5_v308_v6_LocB
from config import rsPath_LA34_tenant6_v515_v4_LocA, rsPath_LA34_tenant6_v515_v4_LocB, rsPath_LA34_tenant6_v515_v6_LocA, rsPath_LA34_tenant6_v515_v6_LocB 
from config import rsPath_LA34_tenant6_v708_v4_LocA, rsPath_LA34_tenant6_v708_v4_LocB, rsPath_LA34_tenant6_v708_v6_LocA, rsPath_LA34_tenant6_v708_v6_LocB
from config import rsPath_LB12_tenant6_v514_v4_LocA, rsPath_LB12_tenant6_v514_v4_LocB, rsPath_LB12_tenant6_v514_v6_LocA, rsPath_LB12_tenant6_v514_v6_LocB
from config import rsPath_LB12_tenant6_v516_v4_LocA, rsPath_LB12_tenant6_v516_v4_LocB, rsPath_LB12_tenant6_v516_v6_LocA, rsPath_LB12_tenant6_v516_v6_LocB 
from config import rsPath_LB12_tenant6_v712_v4_LocA, rsPath_LB12_tenant6_v712_v4_LocB, rsPath_LB12_tenant6_v712_v6_LocA, rsPath_LB12_tenant6_v712_v6_LocB 
from config import ipVpcMemberMappingSite1LA12, ipVpcMemberMappingSite1LA34, ipVpcMemberMappingSite2LB12

class Login:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.cookies = None
        self.cookie_expiry = 0
    
    def getCookie(self):
        current_time = time.time()
        if self.cookies is None or current_time > self.cookie_expiry:
            body =  {
                "aaaUser": 
                    {
                        "attributes": {
                            "name": self.username, "pwd": self.password
                            }
                    }
            }
            login_url = "https://" + self.url + "/api/aaaLogin.json"
            login_response = requests.post(login_url, json=body, verify=False)
            response_body = login_response.content
            response_body_dictionary = json.loads(response_body)
            token = response_body_dictionary["imdata"][0]["aaaLogin"]["attributes"]["token"]
            cookies = {"APIC-cookie": token}
            self.cookies = cookies
            self.cookie_expiry = current_time + 550
        return self.cookies

class BorderLeaf(Login):

    def __init__(self, nodeName, nodeId, siteName, podId, siteIpAddress, username, password):
        super().__init__(siteIpAddress, username, password)
        self.nodeName = nodeName
        self.nodeId = nodeId
        self.siteName = siteName
        self.podId = podId
        self.siteIpAddress = siteIpAddress
        self.cookies = None
        self._bgpUrl = None
        #self.side = None  # configured Side (A/B)
        #self.rsPathUrl = None
        #self.rsPathConfigFileLocation = None
  
    def setSide(self, side):
        self.side = side

    @property
    def bgpUrl(self):
        return self._bgpUrl

    @bgpUrl.setter
    def bgpUrl(self, url):
        self._bgpUrl = url
    
    def getNodeState(self): 
        '''
        Retrieve ACI leaf state, focusing on active and inactive state.
        '''
        payload = ""
        cookies = self.getCookie()
        url = "https://" + self.siteIpAddress + \
            "/api/node/class/fabricNode.json?query-target-filter=and(wcard(fabricNode.dn," + "\"node-" + str(self.nodeId) + "\"))"
        payload = ""

        try:
            response = requests.get(url, cookies=cookies, data=payload, verify=False)
            response.raise_for_status()
            result = json.loads(response.text)
            return result["imdata"][0]["fabricNode"]["attributes"]["fabricSt"]
    
        except requests.exceptions.HTTPError as err:
            print("HTTP error occurred:", err)
    
        except requests.exceptions.ConnectionError as err:
            print("Connection error occurred:", err)
    
        except requests.exceptions.Timeout as err:
            print("Timeout error occurred:", err)

        except requests.exceptions.RequestException as err:
            print("An error occurred:", err)

    def getBgpState(self):
        payload = ""
        cookies = self.getCookie()
        url = self.bgpUrl
        if url:
            try:
                response = requests.get(url, cookies=cookies, data=payload, verify=False)
                response.raise_for_status()
                result = json.loads(response.text)
                #print(result)
                return result["imdata"][0]["bgpPeerEntry"]["attributes"]["operSt"]

            except requests.exceptions.HTTPError as err:
                print(f"HTTP error occurred, node {self.nodeName} - {self.nodeId} - {self.siteName} unreachable!")
    
            except requests.exceptions.ConnectionError as err:
                print("Connection error occurred:", err)
    
            except requests.exceptions.Timeout as err:
                print("Timeout error occurred:", err)

            except requests.exceptions.RequestException as err:
                print("An error occurred:", err)

    def display_info(self):
        node_state = self.getNodeState()
        bgp_peering_state = self.getBgpState()
        
        #print("ACI Leaf Information:")
        #print(f"Site Name: {self.siteName}")
        #print(f"Pod ID: {self.podId}")
        print(f"Node Name: {self.nodeName}")
        #print(f"Node ID: {self.nodeId}")
        #print(f"Node State: {node_state}")
        print(f"BGP URL: {self.bgpUrl}")
        print(f"BGP Peering State: {bgp_peering_state}")

    def addRsPath(self, rsPathUrl, rsPathConfigFileLocation):
        '''
        Configure rsPath to change BGP Peering
        '''
        cookies = self.getCookie()
        url = rsPathUrl
        configLocation = rsPathConfigFileLocation
        if url:
            try:
                requests.post(url, cookies=cookies, data=open(configLocation, 'rb'), verify=False)
    
            except requests.exceptions.HTTPError as err:
                print(f"HTTP error occurred, the node {self.nodeId} is unreachable!")
    
            except requests.exceptions.ConnectionError as err:
                print("Connection error occurred:", err)
    
            except requests.exceptions.Timeout as err:
                print("Timeout error occurred:", err)

            except requests.exceptions.RequestException as err:
                print("An error occurred:", err)

    def side_is_down(self):
        '''
        return True if node is not active or its BGP peer peering state is not established
        '''
        if self.getNodeState() != "active":
            return True
        else:
            return False
        
    def side_configuredFlag(self, ipAddress, memA):
        '''
            Return True if side A is configured for BGP peering.
            Else return False
        '''
        cookies = self.getCookie()

        payload = ""

        url = memA
        try:
            response = requests.get(url, cookies=cookies, data=payload, verify=False)
            response.raise_for_status()
            result = json.loads(response.text)
            address = result["imdata"][0]["l3extMember"]["attributes"]["addr"]
            if  ipAddress in address:
                return True
            else:
                return False
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred:", err)
        except requests.exceptions.ConnectionError as err:
            print("Connection error occurred:", err)
    
        except requests.exceptions.Timeout as err:
            print("Timeout error occurred:", err)
        except requests.exceptions.RequestException as err:
            print("An error occurred:", err)
    
def shortenUrl(string):
    match = re.search(r'peer-\[([\w\d:/.]+)\]', string)
    if match:
        peer_string = match.group(1)
        return peer_string
    else:
        print("String not found.")

def monitor_reconfigBgpSite1():
    # LA1 and LA2 are in vpc pair, LA1 is sideA, LA2 is sideB
    # LA3 and LA4 are in vpc pair, LA3 is sideA, LA4 is sideB

    LA1 = BorderLeaf("LA1","1201","site1","1",s1apic, s1user, s1password)
    LA2 = BorderLeaf("LA2","1202","site1","1",s1apic, s1user, s1password)

    LA3 = BorderLeaf("LA3","1203","site1","1",s1apic, s1user, s1password)
    LA4 = BorderLeaf("LA4","1204","site1","1",s1apic, s1user, s1password)

    BorderLeafSite1List = [LA1,LA2,LA3,LA4]

    global LA12_bgp_sideA_configured
    global LA12_bgp_sideB_configured
    global LA34_bgp_sideA_configured
    global LA34_bgp_sideB_configured

    LA12sideAconfiguredStates = []
    for ipAddress, memA in ipVpcMemberMappingSite1LA12.items():
        LA12sideAconfiguredStates.append(LA1.side_configuredFlag(ipAddress, memA))

    if all(LA12sideAconfiguredStates):
        LA12_bgp_sideA_configured = True
        LA12_bgp_sideB_configured = False
    else:
        LA12_bgp_sideA_configured = False
        LA12_bgp_sideB_configured = True
    
    LA34sideAconfiguredStates = []
    for ipAddress, memA in ipVpcMemberMappingSite1LA34.items():
        LA34sideAconfiguredStates.append(LA3.side_configuredFlag(ipAddress, memA))

    if all(LA34sideAconfiguredStates):
        LA34_bgp_sideA_configured = True
        LA34_bgp_sideB_configured = False
    else:
        LA34_bgp_sideA_configured = False
        LA34_bgp_sideB_configured = True

    # check status of BGP configured on side-A and side-B

    while True:
        time.sleep(5)
        for bl in BorderLeafSite1List:
            print(bl.nodeName, "state:", bl.getNodeState())
        # BGP state on LA1
        for url in LA1_bgp_url:
            LA1.bgpUrl = url
            print(f"LA1 BGP peer to",shortenUrl(url),"state:--->", LA1.getBgpState())
        
        # BGP state on LA2
        for url in LA2_bgp_url:
            LA2.bgpUrl = url
            print(f"LA2 BGP peer to",shortenUrl(url),"state:--->", LA2.getBgpState())
        
        # BGP state on LA3
        for url in LA3_bgp_url:
            LA3.bgpUrl = url
            print(f"LA3 BGP peer to",shortenUrl(url),"state:--->", LA3.getBgpState())
        
        # BGP state on LA4
        for url in LA4_bgp_url:
            LA4.bgpUrl = url
            print(f"LA4 BGP peer to",shortenUrl(url),"state:--->",LA4.getBgpState())

        # Monitor side A
        if LA1.side_is_down() and not LA12_bgp_sideB_configured:
            # configure sideB
            LA2.addRsPath(rsPath_LA12_tenant5_v307_v4,rsPath_LA12_tenant5_v307_v4_LocB)
            LA2.addRsPath(rsPath_LA12_tenant5_v307_v6,rsPath_LA12_tenant5_v307_v6_LocB)
            LA2.addRsPath(rsPath_LA12_tenant6_v513_v4,rsPath_LA12_tenant6_v513_v4_LocB)
            LA2.addRsPath(rsPath_LA12_tenant6_v513_v6,rsPath_LA12_tenant6_v513_v6_LocB)
            LA2.addRsPath(rsPath_LA12_tenant6_v704_v4,rsPath_LA12_tenant6_v704_v4_LocB)
            LA2.addRsPath(rsPath_LA12_tenant6_v704_v6,rsPath_LA12_tenant6_v704_v6_LocB)
            LA12_bgp_sideB_configured = True
            LA12_bgp_sideA_configured = False
            print("Configure BGP on Side B - LA2 as Side A got BGP peering issue.")
     
        # Monitor side B
        if LA2.side_is_down() and not LA12_bgp_sideA_configured:
            # configure sideB
            LA1.addRsPath(rsPath_LA12_tenant5_v307_v4,rsPath_LA12_tenant5_v307_v4_LocA)
            LA1.addRsPath(rsPath_LA12_tenant5_v307_v6,rsPath_LA12_tenant5_v307_v6_LocA)
            LA1.addRsPath(rsPath_LA12_tenant6_v513_v4,rsPath_LA12_tenant6_v513_v4_LocA)
            LA1.addRsPath(rsPath_LA12_tenant6_v513_v6,rsPath_LA12_tenant6_v513_v6_LocA)
            LA1.addRsPath(rsPath_LA12_tenant6_v704_v4,rsPath_LA12_tenant6_v704_v4_LocA)
            LA1.addRsPath(rsPath_LA12_tenant6_v704_v6,rsPath_LA12_tenant6_v704_v6_LocA)
            LA12_bgp_sideB_configured = False
            LA12_bgp_sideA_configured = True
            print("Configure BGP on Side A - LA1 as Side B got BGP peering issue.")

         # Monitor side A
        if LA3.side_is_down() and not LA34_bgp_sideB_configured:
            # configure sideB
            LA4.addRsPath(rsPath_LA34_tenant5_v308_v4,rsPath_LA34_tenant5_v308_v4_LocB)
            LA4.addRsPath(rsPath_LA34_tenant5_v308_v6,rsPath_LA34_tenant5_v308_v6_LocB)
            LA4.addRsPath(rsPath_LA34_tenant6_v515_v4,rsPath_LA34_tenant6_v515_v4_LocB)
            LA4.addRsPath(rsPath_LA34_tenant6_v515_v6,rsPath_LA34_tenant6_v515_v6_LocB)
            LA4.addRsPath(rsPath_LA34_tenant6_v708_v4,rsPath_LA34_tenant6_v708_v4_LocB)
            LA4.addRsPath(rsPath_LA34_tenant6_v708_v6,rsPath_LA34_tenant6_v708_v6_LocB)
            LA34_bgp_sideB_configured = True
            LA34_bgp_sideA_configured = False
            print("Configure BGP on Side B - LA4 as Side A got BGP peering issue.")
        
        # Monitor side B
        if LA4.side_is_down() and not LA34_bgp_sideA_configured:
            # configure sideB
            LA3.addRsPath(rsPath_LA34_tenant5_v308_v4,rsPath_LA34_tenant5_v308_v4_LocA)
            LA3.addRsPath(rsPath_LA34_tenant5_v308_v6,rsPath_LA34_tenant5_v308_v6_LocA)
            LA3.addRsPath(rsPath_LA34_tenant6_v515_v4,rsPath_LA34_tenant6_v515_v4_LocA)
            LA3.addRsPath(rsPath_LA34_tenant6_v515_v6,rsPath_LA34_tenant6_v515_v6_LocA)
            LA3.addRsPath(rsPath_LA34_tenant6_v708_v4,rsPath_LA34_tenant6_v708_v4_LocA)
            LA3.addRsPath(rsPath_LA34_tenant6_v708_v6,rsPath_LA34_tenant6_v708_v6_LocA)
            LA34_bgp_sideB_configured = False
            LA34_bgp_sideA_configured = True
            print("Configure BGP on Side A - LA3 as Side B got BGP peering issue.")
        
        time.sleep(10)  # Wait for 10 seconds before the next iteration

def monitor_reconfigBgpSite2():
    # LA1 and LA2 are in vpc pair, LA1 is sideA, LA2 is sideB
    # LA3 and LA4 are in vpc pair, LA3 is sideA, LA4 is sideB

    LB1 = BorderLeaf("LB1","1201","site2","1",s2apic, s2user, s2password)
    LB2 = BorderLeaf("LB2","1202","site2","1",s2apic, s2user, s2password)

    BorderLeafSite2List = [LB1,LB2]

    global LB12_bgp_sideA_configured
    global LB12_bgp_sideB_configured
   
    LB12sideAconfiguredStates = []
    for ipAddress, memA in ipVpcMemberMappingSite2LB12.items():
        LB12sideAconfiguredStates.append(LB1.side_configuredFlag(ipAddress, memA))

    if all(LB12sideAconfiguredStates):
        LB12_bgp_sideA_configured = True
        LB12_bgp_sideB_configured = False
    else:
        LB12_bgp_sideA_configured = False
        LB12_bgp_sideB_configured = True
    
    # check status of BGP configured on side-A and side-B

    while True:
        time.sleep(5)
        for bl in BorderLeafSite2List:
            print(bl.nodeName, "state:", bl.getNodeState())

        # BGP state on LB1
        for url in LB1_bgp_url:
            LB1.bgpUrl = url
            print(f"LB1 BGP peer to",shortenUrl(url),"state:--->", LB1.getBgpState())
        
        # BGP state on LB2
        for url in LB2_bgp_url:
            LB2.bgpUrl = url
            print(f"LB2 BGP peer to",shortenUrl(url),"state:--->", LB2.getBgpState())
        
        # Monitor side A
        if LB1.side_is_down() and not LB12_bgp_sideB_configured:
            # configure sideB
            LB2.addRsPath(rsPath_LB12_tenant6_v514_v4,rsPath_LB12_tenant6_v514_v4_LocB)
            LB2.addRsPath(rsPath_LB12_tenant6_v514_v6,rsPath_LB12_tenant6_v514_v6_LocB)
            LB2.addRsPath(rsPath_LB12_tenant6_v516_v4,rsPath_LB12_tenant6_v516_v4_LocB)
            LB2.addRsPath(rsPath_LB12_tenant6_v516_v6,rsPath_LB12_tenant6_v516_v6_LocB)
            LB2.addRsPath(rsPath_LB12_tenant6_v712_v4,rsPath_LB12_tenant6_v712_v4_LocB)
            LB2.addRsPath(rsPath_LB12_tenant6_v712_v6,rsPath_LB12_tenant6_v712_v6_LocB)
            LB12_bgp_sideB_configured = True
            LB12_bgp_sideA_configured = False
            print("Configure BGP on Side B - LB2 as Side A got BGP peering issue.")
        
        # Monitor side B
        if LB2.side_is_down() and not LB12_bgp_sideA_configured:
            # configure sideB
            LB1.addRsPath(rsPath_LB12_tenant6_v514_v4,rsPath_LB12_tenant6_v514_v4_LocA)
            LB1.addRsPath(rsPath_LB12_tenant6_v514_v6,rsPath_LB12_tenant6_v514_v6_LocA)
            LB1.addRsPath(rsPath_LB12_tenant6_v516_v4,rsPath_LB12_tenant6_v516_v4_LocA)
            LB1.addRsPath(rsPath_LB12_tenant6_v516_v6,rsPath_LB12_tenant6_v516_v6_LocA)
            LB1.addRsPath(rsPath_LB12_tenant6_v712_v4,rsPath_LB12_tenant6_v712_v4_LocA)
            LB1.addRsPath(rsPath_LB12_tenant6_v712_v6,rsPath_LB12_tenant6_v712_v6_LocA)
            LB12_bgp_sideB_configured = False
            LB12_bgp_sideA_configured = True
            print("Configure BGP on Side A - LB1 as Side B got BGP peering issue.")

        time.sleep(10)  # Wait for 10 seconds before the next iteration

def main_threading():
    thread1 = threading.Thread(target=monitor_reconfigBgpSite1)
    thread2 = threading.Thread(target=monitor_reconfigBgpSite2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

def main():
    print("====================================================")    
    print(f"Border Leaf BGP peering state and fabric node state:")
    main_threading()

if __name__ == "__main__":
    main()