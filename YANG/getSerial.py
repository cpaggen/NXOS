#!/usr/bin/env python

import sys
from ncclient import manager

DEVICES = ['10.48.168.22']
USER = 'automation'
PASS = 'cisco'
PORT = 830

def main():

    serial_number = """
        <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
          <serial/>
        </System>
    """

    for device in DEVICES:
        with manager.connect(host=device, port=PORT, username=USER,
                             password=PASS, hostkey_verify=False,
                             device_params={'name': 'nexus'},
                             look_for_keys=False, allow_agent=False) as m:

            netconf_response = m.get(('subtree', serial_number))
            xml_data = netconf_response.data_ele
            serial = xml_data.find(".//{http://cisco.com/ns/yang/cisco-nx-os-device}serial").text
            print(f"The serial number for {device} is {serial}")

if __name__ == '__main__':
    sys.exit(main())

