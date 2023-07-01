import requests
import json
import time
from config import APIC, user, password, BorderLeaf

requests.packages.urllib3.disable_warnings()

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


def getNodeState(nodeId, podId = 1):
    '''
    Returns fabric State of node whose id is nodeId in Pod PodId
    podId and nodeId are string type number
    '''
    cookies = getCookie()

    url = "https://" + APIC + \
        "/api/node/mo/topology/pod-" +str(podId) + "/node-" + str(nodeId) + ".json?query-target=self"
    payload = ""
    
    response = requests.get(url, cookies=cookies, data=payload, verify=False)
    result = json.loads(response.text)
    return result["imdata"][0]["fabricNode"]["attributes"]["fabricSt"]

def main():
    
    print(f"Border Leaf Node fabric state:")

    while True:
        time.sleep(30)
        for nodeId, nodeName in BorderLeaf.items():
            nodeState = getNodeState(nodeId)
            print(f"Border Leaf",nodeName, "Node ID",nodeId, "state:", nodeState )


if __name__ == "__main__":
    main()