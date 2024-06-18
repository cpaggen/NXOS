from pprint import pprint
from pygnmi.client import gNMIclient

INVENTORY = {
                "host": "10.48.168.22",
                "auth_username": "automation",
                "auth_password": "cisco",
                "port": 50051
            }

# note: we rely on the NXOS auto-provisioned self-signed cert
#       with 1-day validity that gets installed when feature grpc
#       is enabled in the NXOS configuration. For prod, please
#       replace with proper certs!

if __name__ == "__main__":
    with gNMIclient(target=(INVENTORY["host"], INVENTORY["port"]),
                    username=INVENTORY["auth_username"],
                    password=INVENTORY["auth_password"],
                    skip_verify=True) as gconn:
        pprint(gconn.capabilities())
        pprint(gconn.get(path=["/System/cdp-items"]))
