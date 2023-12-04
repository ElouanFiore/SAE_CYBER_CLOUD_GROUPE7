import requests

"""
1: api key
2: ip elastic
3; mdp elastic
4: id de la fleet
"""

header={"Content-Type":"application/json","Authorisation":f"ApiKey {sys.argv[1]}","kbn-xsrf:xx"}
r=requests.get(f"https://{sys.argv[2]}:9200/api/fleet/enrollment_api_keys",auth=("elastic":sys.argv[3]),headers=headers)
data=r.content.decode()
for i in range(lan(data["items"])):
    if data["items"][i]["id"]= sys.argv[4]:
        print(data["items"][i]["api_key"])
