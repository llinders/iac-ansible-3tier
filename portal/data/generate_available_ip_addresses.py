import json

addresses = []
for i in range(10, 200):
    addresses.append("10.0.0." + str(i))

dict = {
    "available_ip_addresses": addresses
}

with open('portal/data/available_ip_addresses.json', 'w') as outfile:
    json.dump(dict, outfile, indent=4)