from pprint import pprint
from pygnmi.client import gNMIclient
import re

pattern = r"eth(\d+)/(\d+)"

inventory = [{
                "host": "10.48.168.22",
                "auth_username": "automation",
                "auth_password": "cisco",
                "port": 50051
            },
            {
                "host": "10.48.168.101",
                "auth_username": "automation",
                "auth_password": "cisco",
                "port": 50051
            },
            {
                "host": "10.48.168.250",
                "auth_username": "automation",
                "auth_password": "cisco",
                "port": 50051
            }]

# note: we rely on the NXOS auto-provisioned self-signed cert
#       with 1-day validity that gets installed when feature grpc
#       is enabled in the NXOS configuration. For prod, please
#       replace with proper certs!

if __name__ == "__main__":
    for device in inventory:
        with gNMIclient(target=(device["host"], device["port"]),
                        username=device["auth_username"],
                        password=device["auth_password"],
                        skip_verify=True) as gconn:
            print(f"LLDP entries for {device['host']}:")
            lldp = gconn.get(path=["/System/lldp-items/inst-items/if-items/If-list/adj-items/AdjEp-list/sysName"])
            for neighbor in lldp['notification'][0]['update']:
                path = neighbor['path']
                dev  = neighbor['val']
                match = re.search(pattern, path)
                if match:
                    print(f"{match.group(0)} ==> {dev}")


