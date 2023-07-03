import requests
import json
import time
from config import s1apic, s1user, s1password, s1BorderLeaf, s2apic, s2user, s2password, s2BorderLeaf
requests.packages.urllib3.disable_warnings()

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


def getNodeState(nodeId, site="site1"):
    '''
    Returns fabric State of node whose id is nodeId in Pod PodId
    podId and nodeId are string type number
    '''
    login1 = Login(s1apic, s1user, s1password)
    login2 = Login(s2apic, s2user, s2password)

    cookies1 = login1.getCookie()
    cookies2 = login2.getCookie()
    
    if site == "site1":
        cookies = cookies1  
        apic = s1apic

    elif site == "site2":
        cookies = cookies2
        apic = s2apic

    url = "https://" + apic + \
    "/api/node/class/fabricNode.json?query-target-filter=and(wcard(fabricNode.dn," + "\"node-" + str(nodeId) + "\"))"
    
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

def getBgpState(nodeId, site="site1", ipv="v4"):
    '''
    Check BGP peer state from leaf with both IPv4 and IPv6
    Return Operational State such as established/idle
    '''

    login1 = Login(s1apic, s1user, s1password)
    login2 = Login(s2apic, s2user, s2password)

    cookies1 = login1.getCookie()
    cookies2 = login2.getCookie()

    if site == "site1":
        cookies = cookies1
        apic = s1apic

    elif site == "site2":
        cookies = cookies2
        apic = s2apic
    if ipv == "v4":
        url = "https://" + apic + \
            "/api/node/mo/topology/pod-1/node-" + str(nodeId) + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1806/peer-[16.16.4.10/32]/ent-[16.16.4.10].json?query-target=self"
    elif ipv == "v6":
        url = "https://" + apic + \
            "/api/node/mo/topology/pod-1/node-"+ str(nodeId) + \
            "/sys/bgp/inst/dom-tenant-6:vrf-6-1806/peer-[2002::16:16:4:10/128]/ent-[2002::16:16:4:10].json?query-target=self"
        
    payload = ""

    try:
        response = requests.get(url, cookies=cookies, data=payload, verify=False)
        response.raise_for_status()
        result = json.loads(response.text)
        return result["imdata"][0]["bgpPeerEntry"]["attributes"]["operSt"]

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred, the node {str(nodeId)} is unreachable!")
    
    except requests.exceptions.ConnectionError as err:
        print("Connection error occurred:", err)
    
    except requests.exceptions.Timeout as err:
        print("Timeout error occurred:", err)

    except requests.exceptions.RequestException as err:
        print("An error occurred:", err)


def addRsPath(ipv="v4", site="site1", side="A"):
    '''
    Configure rsPath sideA/B, site1/site2, ipv4/ipv6
    '''

    login1 = Login(s1apic, s1user, s1password)
    login2 = Login(s2apic, s2user, s2password)

    cookies1 = login1.getCookie()
    cookies2 = login2.getCookie()

    if site == "site1":
        cookies = cookies1
        apic = s1apic

    elif site == "site2":
        cookies = cookies2
        apic = s2apic
    
    if ipv == "v4":
        url = "https://" + apic + \
            "/api/node/mo/uni/tn-tenant-6/out-L3OUT-LA12-v704/lnodep-node-1201-1202/lifp-svi-P3_3-vlan-704-v4.json"
        if side == "A":
            configLocation = "configs/addRsPathAv4.json"
        elif side == "B":
            configLocation = "configs/addRsPathBv4.json"

    elif ipv == "v6":
        url = "https://" + apic + \
            "/api/node/mo/uni/tn-tenant-6/out-L3OUT-LA12-v704/lnodep-node-1201-1202/lifp-svi-P3_3-vlan-704-v6.json"
        if side == "A":
            configLocation = "configs/addRsPathAv6.json"
        elif side == "B":
            configLocation = "configs/addRsPathBv6.json"
    
    requests.post(url, cookies=cookies, data=open(configLocation, 'rb'), verify=False)


def sideA_is_down():
    '''
    return True if LA1 is not active or its BGP peer peering state is not established
    '''
    '''
    LA1_bgpPeerStateV4 = getBgpState("1201", site="site1", ipv="v4")
    print(f"LA1 1201 has BGP IPv4 state: ", LA1_bgpPeerStateV4)

    LA1_bgpPeerStateV6 = getBgpState("1201", site="site1", ipv="v6")
    print(f"LA1 1201 has BGP IPv6 state: ", LA1_bgpPeerStateV6)
    '''
    LA1_nodeState = getNodeState("1201", "site1")
    print(f"LA1 fabric Node state: ", LA1_nodeState)
   
    if LA1_nodeState != "active":
        return True
    else:
        return False

def sideB_is_down():
    '''
    return True if LA2 is not active or its BGP peer peering state is not established
    '''
    '''
    LA2_bgpPeerStateV4 = getBgpState("1202", site="site1", ipv="v4")
    print(f"LA2 1202 has BGP IPv4 state: ", LA2_bgpPeerStateV4)

    LA2_bgpPeerStateV6 = getBgpState("1202", site="site1", ipv="v6")
    print(f"LA2 1202 has BGP IPv6 state: ", LA2_bgpPeerStateV6)
    '''
    LA2_nodeState = getNodeState("1202", "site1")
    print(f"LA2 fabric Node state: ", LA2_nodeState)

    if  LA2_nodeState != "active":
        return True
    else:
        return False

def configure_sideA():
    addRsPath(ipv="v4", site="site1", side="A")
    addRsPath(ipv="v6", site="site1", side="A")

def configure_sideB():
    addRsPath(ipv="v4", site="site1", side="B")
    addRsPath(ipv="v6", site="site1", side="B")


def monitor_reconfigBgp():

    global bgp_sideA_configured
    global bgp_sideB_configured

    # check status of BGP configur on side-A and side-B
    LA1_bgpPeerStateV4 = getBgpState("1201", site="site1", ipv="v4")
    LA2_bgpPeerStateV4 = getBgpState("1202", site="site1", ipv="v4")

    if LA1_bgpPeerStateV4 == "established":
        bgp_sideB_configured = False
        bgp_sideA_configured = True
    else:
        bgp_sideB_configured = True
        bgp_sideA_configured = False

    while True:
        time.sleep(10)
       
        print("LA1 BGP peering state:",LA1_bgpPeerStateV4)
        print("SideA configured state:", bgp_sideA_configured)
        print("-------------******---------------")
        print("LA2 BGP peering state:",LA2_bgpPeerStateV4)
        print("SideB configured state:", bgp_sideB_configured)
        print("-------------******---------------")

         # Monitor side A
        if sideA_is_down() and not bgp_sideB_configured:
            configure_sideB()
            bgp_sideB_configured = True  
            bgp_sideA_configured = False
            print("Configure BGP on Side B as Side A got BGP peering issue.")
            print(f"Side B Configured:", bgp_sideB_configured)
        
        # Monitor side B
        if sideB_is_down() and not bgp_sideA_configured:
            configure_sideA()
            bgp_sideA_configured = True
            bgp_sideB_configured = False
            print("Configure BGP on Side A as Side B got BGP peering issue.")
            print(f"Side A Configured:", bgp_sideA_configured)
        
        time.sleep(10)  # Wait for 10 seconds before the next iteration

def main():
    print("==============================================================")
   
    print(f"Border Leaf BGP peering state and fabric node state:")

    monitor_reconfigBgp()
    
    
if __name__ == "__main__":
    main()