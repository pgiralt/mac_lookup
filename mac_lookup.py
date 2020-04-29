from requests import get
from urllib3.exceptions import HTTPError as BaseHTTPError
import json
import re
import argparse
import sys
import os


def is_valid_mac_address(input_mac):
    mac_regex = '^((([a-fA-F0-9][a-fA-F0-9]+[-]){5}|([a-fA-F0-9][a-fA-F0-9]+[:]){5})([a-fA-F0-9][a-fA-F0-9])$)|(^([a-fA-F0-9][a-fA-F0-9][a-fA-F0-9][a-fA-F0-9]+[.]){2}([a-fA-F0-9][a-fA-F0-9][a-fA-F0-9][a-fA-F0-9]))$'

    match_result = re.search(mac_regex, input_mac)

    if match_result is not None:
        valid = True
    else:
        valid = False

    return valid


def lookup_mac_address(api_key, mac_address):
    url = f'https://api.macaddress.io/v1?apiKey={api_key}&output=json&search={mac_address}'

    result = False

    try:
        resp = get(url, timeout=10)
        response_data = json.loads(resp.text)

        if resp.status_code == 200:
            if "vendorDetails" in response_data:
                company_name = response_data['vendorDetails']['companyName']

                if company_name != "":
                    print(f'MAC address {mac_address} belongs to {company_name}')
                    print()
                    print("Vendor Details:")
                    for key, value in response_data['vendorDetails'].items():
                        print(f'    {key}: {value}')

                    if "blockDetails" in response_data:
                        print("Block Details:")
                        for key, value in response_data['blockDetails'].items():
                            print(f'    {key}: {value}')
                else:
                    print(f'No company found for MAC address {mac_address}')
                    print()

                if "macAddressDetails" in response_data:
                    print("MAC Address Details:")
                    for key, value in response_data['macAddressDetails'].items():
                        print(f'    {key}: {value}')

                result = True

        else:
            print("Error occurred when attempting to lookup MAC address.")
            print()
            print("Response Code: " + str(resp.status_code))
            print('Error Details:')
            print(resp.text)

    except:
        print("Error occurred connecting to macaddress.io. Ensure you have proper network connectivity.")

    return result


def main():
    api_key = os.environ.get("MACADDRESS_IO_API_KEY")
    result = False

    if api_key is None:
        print("Environment variable MACADDRESS_IO_API_KEY must contain API key from https://macaddress.io/api")
        result = False
    else:
        parser = argparse.ArgumentParser(
            description='Look up the company name ane details associated with a MAC address.')
        parser.add_argument('mac_address')
        args = parser.parse_args()

        mac_address = args.mac_address

        if not is_valid_mac_address(mac_address):
            print(
                mac_address + " is not a properly formatted MAC address. "
                              "Please provide in one of the following formats:")
            print("   XX-XX-XX-XX-XX-XX")
            print("   XX:XX:XX:XX:XX:XX")
            print("   XXXX.XXXX.XXXX")
        else:
            result = lookup_mac_address(api_key, mac_address)

    return result


if __name__ == '__main__':
    status = main()
    sys.exit(status)

