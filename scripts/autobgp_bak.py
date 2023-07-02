import sys
import time
import schedule
import threading
import websocket
import ssl
import json
import urllib.parse
import concurrent.futures
from addRsPathB import addRsPathB
from addRsPathA import addRsPathA

__author__ = 'huyeduon'
#!/usr/bin/env python

# Kindly make sure that you have the modules threading and websocket client installed also.  "pip install threading"    "pip install websocket-client"
# Please use python 3

import requests
from config import APIC, user, password
requests.packages.urllib3.disable_warnings()

# Ensure using python3
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

URL = "https://" + APIC + "/api/aaaLogin.json"
BODY = {"aaaUser": {"attributes": {"name": user, "pwd": password}}}

# websocket_url = "wss://" + APIC + "/socket{}".format(token)


def getCookie():
    global cookie
    global token
    login_response = requests.post(URL, json=BODY, verify=False)
    response_body = login_response.content
    # convert response_body to a dict
    response_body_dictionary = json.loads(response_body)
    token = response_body_dictionary["imdata"][0]["aaaLogin"]["attributes"]["token"]
    cookie = {"APIC-cookie": token}
    return cookie


def getNodeState(podId, nodeId):
    '''
    Returns fabric State of node whose id is nodeId in Pod PodId
    podId and nodeId are string type number
    '''
    cookies = getCookie()

    url = "https://" + APIC + \
        "/api/node/mo/topology/pod-" + \
        str(podId) + "/node-" + str(nodeId) + ".json?query-target=self"
    payload = ""

    response = requests.get(url, cookies=cookies, data=payload, verify=False)
    result = json.loads(response.text)
    return result["imdata"][0]["fabricNode"]["attributes"]["fabricSt"]


def WSocket():
    # This module starts the initial connect to the APIC Web Socket
    global ws
    websocket_url = "wss://" + APIC + "/socket{}".format(token)
    ws = websocket.create_connection(
        websocket_url, sslopt={"cert_reqs": ssl.CERT_NONE})
    print("WebSocket Subscription Status Code: ", ws.status)


def Subscribe():
    # This module subscribes to interested objects in ACI

    global node101_1_53_subscription_id
    global node101_1_54_subscription_id
    global node101_subscription_id

    node101_1_53_url = "https://" + APIC + \
        "/api/node/mo/topology/pod-1/node-101/sys/phys-[eth1/53].json?query-target=self&subscription=yes"
    node101_1_53_subscription = requests.get(
        node101_1_53_url, verify=False, cookies=cookie)
    json_dict = json.loads(node101_1_53_subscription.text)
    node101_1_53_subscription_id = json_dict["subscriptionId"]
    print("Node101_1_53_Subscription ID: ",
          node101_1_53_subscription_id)

    node101_1_54_url = "https://" + APIC + \
        "/api/node/mo/topology/pod-1/node-101/sys/phys-[eth1/54].json?query-target=self&subscription=yes"
    node101_1_54_subscription = requests.get(
        node101_1_54_url, verify=False, cookies=cookie)
    json_dict = json.loads(node101_1_54_subscription.text)
    node101_1_54_subscription_id = json_dict["subscriptionId"]
    print("Node101_1_54_Subscription ID: ",
          node101_1_54_subscription_id)

    node101_url = "https://" + APIC + \
        "/api/node/mo/topology/pod-1/node-101.json?query-target=self&subscription=yes"
    node101_subscription = requests.get(
        node101_url, verify=False, cookies=cookie)
    json_dict = json.loads(node101_subscription.text)
    node101_subscription_id = json_dict["subscriptionId"]
    print("Node101_Subscription ID: ",
          node101_subscription_id)

    print("\n" * 2)


def printws():
    json_string = ''
    uplinkStates = {}
    while True:
        json_string = ws.recv()
        print(ws.recv())
        stateDict = json.loads(json_string)
        #print(stateDict)

        if "eth1/53" in stateDict["imdata"][0]["l1PhysIf"]["attributes"]["dn"] and stateDict["imdata"][0]["l1PhysIf"]["attributes"]["status"] == "modified":
            uplinkStates['Port_1_53'] = "disabled"
        if "eth1/54" in stateDict["imdata"][0]["l1PhysIf"]["attributes"]["dn"] and stateDict["imdata"][0]["l1PhysIf"]["attributes"]["status"] == "modified":
            uplinkStates['Port_1_54'] = "disabled"

        for k, v in uplinkStates.items():
            print(k, v)


def refresh():
    # This module refreshes the subscription.  Default Timeout for refresh is 60 seconds as also hardcoded in the subscription module "refresh-timeout=60"
    while True:
        time.sleep(10)
        # refresh subscription  -- node - Status
        node101_1_53_refresh_url = "https://" + APIC + \
            "/api/subscriptionRefresh.json?id={}".format(
                node101_1_53_subscription_id)
        node101_1_53_refresh_response = requests.get(
            node101_1_53_refresh_url, verify=False, cookies=cookie)

        node101_1_54_refresh_url = "https://" + APIC + \
            "/api/subscriptionRefresh.json?id={}".format(
                node101_1_54_subscription_id)
        node101_1_54_refresh_response = requests.get(
            node101_1_54_refresh_url, verify=False, cookies=cookie)


def startThreading():
    th = threading.Thread(target=printws)
    th1 = threading.Thread(target=refresh)
    #th3 = threading.Thread(target=getNodeState, args=(1, 101))
    th.start()
    th1.start()
    #th3.start()
    #with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit the function to the executor
    #    future = executor.submit(getNodeState, 1, 101)
    # Retrieve the result
    #    result = future.result()

    #print(f"Node fabricState:", result)


if __name__ == "__main__":
    cookie = getCookie()
    token = (cookie["APIC-cookie"])
    print("\n" * 2)
    print("*" * 10, "WebSocket Subscription Status & Messages", "*" * 10)
    WSocket()
    Subscribe()
    startThreading()
    while True:
        time.sleep(60)
        nodeState = getNodeState(1, 101)
        if nodeState == "active":
            print(f"Node 101 in active state")
        else:
            print(
                f"Node 101 in in-active, BGP will be reconfigured to peer from Node 102")
            addRsPathB()
