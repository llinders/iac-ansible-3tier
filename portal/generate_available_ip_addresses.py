import json

addresses = []
for i in range(2, 255):
    addresses.append("192.168.1." + str(i))

dict = {
    "available_ip_addresses": addresses
}

with open('portal/available_ip_addresses.json', 'w') as outfile:
    json.dump(dict, outfile, indent=4)