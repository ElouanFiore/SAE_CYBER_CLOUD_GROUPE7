import requests
import json
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
1: api key
2: ip elastic
3; mdp elastic
"""

auth=("elastic",sys.argv[3])
header={"Content-Type":"application/json","Authorisation":f"ApiKey {sys.argv[1]}","kbn-xsrf":"xx"}
r=requests.get(f"https://{sys.argv[2]}:5601/api/fleet/enrollment_api_keys",auth=auth,headers=header,verify=False)
data=json.loads(r.content.decode())
for i in range(len(data["list"])):
    if data["list"][i]["policy_id"] == "GOAD-SRV":
        print(data["list"][i]["api_key"])
