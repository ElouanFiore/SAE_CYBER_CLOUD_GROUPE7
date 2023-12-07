#!/bin/python3
import requests
import sys
import json
headers={"Content-Type":"application/json",
        "Accept":"*/*",
        "Authorization":f"ApiKey {sys.argv[2]}",
        "Cache-Control":"no-cache",
        "Connection":"keep-alive",
        "kbn-xsrf":"xxx"}
data='{"name": "GOAD-SRV","id":"GOAD-SRV","description": "","namespace": "default","monitoring_enabled": ["logs", "metrics"]}'
auth=("elastic",sys.argv[1])
r=requests.post(f"https://{sys.argv[3]}:5601/api/fleet/agent_policies?sys_monitoring=true",auth=auth,headers=headers,data=data,verify=False)
print(r.content.decode())
