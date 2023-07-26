import requests
import json
import time
requests.packages.urllib3.disable_warnings()
la1="100.64.46.102"
user="admin"
password="123Cisco123"
import time

from threading import Thread


class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
            
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

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
    
def getPortState(eth):
    login = Login(la1, user, password)
    cookies = login.getCookie()
    url = "https://100.64.46.102/api/node/mo/sys/phys-[eth1/" + str(eth) + "]/phys.json?query-target=self"
    payload = ""
    try:
        response = requests.get(url, cookies=cookies, data=payload, verify=False)
        response.raise_for_status()
        result = json.loads(response.text)
        return "Eth1/" + str(eth) + " last state change at:" + "--> " + result["imdata"][0]["ethpmPhysIf"]["attributes"]["lastLinkStChg"]

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred, the node", err)
    
    except requests.exceptions.ConnectionError as err:
        print("Connection error occurred:", err)
    
    except requests.exceptions.Timeout as err:
        print("Timeout error occurred:", err)

    except requests.exceptions.RequestException as err:
        print("An error occurred:", err)


def main():
    threads = []
    #eth= [1,3,6,7,8,9,11,13,16,17,18,19,27,35,36,37,38,40,43,45,49]
    #ethvpc = [1,3,6]
    eth= [2,12,31,32,36,38,1,3,6]
    for e in eth:
        t = CustomThread(target=getPortState, args=(e,))
        t.start()
        threads.append(t)
    for t in threads:
        print(t.join())

    
if __name__ == "__main__":
    main()