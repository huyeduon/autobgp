import requests
import json
import time
from config import s1apic, s1user, s1password, s1BorderLeaf, s2apic, s2user, s2password, s2BorderLeaf
requests.packages.urllib3.disable_warnings()
'''
URL = "https://" + APIC + "/api/aaaLogin.json"
BODY = {"aaaUser": {"attributes": {"name": user, "pwd": password}}}


def getCookie():
    global cookie
    global token
    login_response = requests.post(URL, json=BODY, verify=False)
    response_body = login_response.content
    response_body_dictionary = json.loads(response_body)
    token = response_body_dictionary["imdata"][0]["aaaLogin"]["attributes"]["token"]
    cookie = {"APIC-cookie": token}
    return cookie
'''
class Login:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
    
    def getCookie(self):
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
        return cookies

login1 = Login(s1apic, s1user, s1password)
login2 = Login(s2apic, s2user, s2password)

cookies1 = login1.getCookie()
cookies2 = login2.getCookie()

def getNodeState(nodeId, site="site1"):
    '''
    Returns fabric State of node whose id is nodeId in Pod PodId
    podId and nodeId are string type number
    '''
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


def addRsPath(ipv="v4", site="site1", side="A"):
    '''
    Configure rsPath sideA/B, site1/site2, ipv4/ipv6
    '''

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
    

def main():
    print("==============================================================")
    '''
    print(f"Configure Site1 SideA IPv4")
    addRsPath("v4","site1","A")

    time.sleep(2)
    print(f"Configure Site1 SideA IPv6")
    addRsPath("v6", "site1", "A")
    '''
    print(f"Border Leaf Node fabric state:")

    while True:
        time.sleep(10)
        for nodeId, nodeName in s1BorderLeaf.items():
            nodeState = getNodeState(nodeId, "site1")
            print(f"Site 1 Node", nodeName, nodeState)

        for nodeId, nodeName in s2BorderLeaf.items():
            nodeState = getNodeState(nodeId, "site2")
            print(f"Site 2 Node", nodeName, nodeState)

    
if __name__ == "__main__":
    main()