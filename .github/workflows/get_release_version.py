import json

with open("./endpoint.json", "r") as f:
    data = json.load(f)

print("Version " + ".".join(data["versions"][0]["version"]))