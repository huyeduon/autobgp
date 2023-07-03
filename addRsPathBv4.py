import requests
import json
requests.packages.urllib3.disable_warnings()

APIC = "100.64.46.11"
user = "admin"
password = "123Cisco123"

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


def addRsPathB():
    cookies = getCookie()
    url = "https://" + APIC + \
        "/api/node/mo/uni/tn-tenant-6/out-L3OUT-LA12-v704/lnodep-node-1201-1202/lifp-svi-P3_3-vlan-704-v4.json"

    requests.post(url, cookies=cookies, data=open(
        'configs/addRsPathBv4.json', 'rb'), verify=False)


def main():
    addRsPathB()


if __name__ == '__main__':
    main()
