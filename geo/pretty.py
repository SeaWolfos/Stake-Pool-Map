import json

with open('./geoResponse.txt') as f:
    data = json.load(f)
    print(json.dumps(data, indent = 4, sort_keys=True))
