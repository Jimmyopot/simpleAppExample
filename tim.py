import json

results = []

data = {
    "name": "name",
    "date": "date",
    "born": "born"
}

results.append(data)

with open("package_info.json", "w") as f:
    json.dump(results, f, indent=1)