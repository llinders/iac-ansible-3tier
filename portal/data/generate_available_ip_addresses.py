import json

addresses = []
for i in range(10, 200):
    addresses.append("10.0.0." + str(i))

with open('portal/data/available_ip_addresses.json', 'w') as outfile:
    json.dump(addresses, outfile, indent=4)