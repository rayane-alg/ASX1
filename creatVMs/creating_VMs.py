print("hello world")

import requests
import urllib3
import argparse
from vmware.vapi.vsphere.client import create_vsphere_client

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def list_vms(hostname, username, password):
    # Create a session
    session = requests.session()
    session.verify = False  # Disable SSL verification (not recommended for production)

    # Create the vSphere client
    vsphere_client = create_vsphere_client(hostname, username, password, session=session)

    # List all VMs
    vms = vsphere_client.vcenter.VM.list()
    return vms

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='List VMs in vSphere environment.')
    parser.add_argument('-s', '--server', required=True, help='vCenter server hostname or IP')
    parser.add_argument('-u', '--username', required=True, help='Username for vCenter')
    parser.add_argument('-p', '--password', required=True, help='Password for vCenter')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')

    args = parser.parse_args()

    # List VMs
    vms = list_vms(args.server, args.username, args.password)

    # Print VM details
    for vm in vms:
        if args.verbose:
            print(f"VM ID: {vm.vm}, Name: {vm.name}, Power State: {vm.power_state}")
        else:
            print(f"VM Name: {vm.name}")

if __name__ == "__main__":
    main()



























