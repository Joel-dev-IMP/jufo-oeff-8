import json
import os

INIT_PATH = "./__init__.py"
ENDPOINT_PATH = "./endpoint.json"
repo_url = "jufo-oeff-8"

def get_new_version(old_version) -> list:
    if old_version[-1] <= 9:
        return [old_version[0], old_version[1], old_version[2] + 1]

    if old_version[-2] <= 9: 
        return [old_version[0], old_version[1] + 1, 0]

    return [old_version[0] + 1, 0, 0]

with open(ENDPOINT_PATH, "r") as f:
    endpoint_data: dict = json.load(f)

old_version = endpoint_data["versions"][0]["version"]

new_version = get_new_version(old_version)
new_version_str = "_".join([str(x) for x in new_version])
print(new_version_str)

with open(INIT_PATH, "r") as f:
    data: str = f.read()

data = data.replace(f"({old_version[0]}, {old_version[1]}, {old_version[2]})", f"({new_version[0]}, {new_version[1]}, {new_version[2]})")

with open(INIT_PATH, "w+") as f:
    f.write(data)

new_endpoint_version = {
    "version": new_version,
    "allow_automatic_download": True,
    "download_url": f"https://github.com/Joel-dev-IMP/{repo_url}/releases/download/{new_version_str}/{repo_url}.zip",
    "minimum_blender_version": [
        2,
        83,
        0
    ]
}

with open(ENDPOINT_PATH, "r") as f:
    endpoint_data = json.load(f)

endpoint_data["versions"].insert(0, new_endpoint_version)

with open(ENDPOINT_PATH, "w+") as f:
    json.dump(endpoint_data, f, indent=4)
