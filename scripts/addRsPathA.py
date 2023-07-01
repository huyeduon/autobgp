import requests
import json
from config import APIC, user, password
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

def addRsPathA():
    cookies = getCookie()
    url = "https://" + APIC + \
        "/api/node/mo/uni/tn-demo/out-tfbgp/lnodep-tfbgp_nodeProfile/lifp-tfbgp_vpcIpv4.json"

    requests.post(url, cookies=cookies, data=open(
        'configs/addRsPathA.json', 'rb'), verify=False)

def main():
    addRsPathA()


if __name__ == '__main__':
    main()
