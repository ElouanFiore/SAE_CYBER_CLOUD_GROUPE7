import json

with open("test.json") as f:
    data=f.read()
    data=json.loads(data)
    print(list(data["ansible_facts"]["ansible_env"]))
