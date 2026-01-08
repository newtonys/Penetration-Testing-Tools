import requests
import sys

subdomain_list = open(sys.argv[2]).read()
subdomains = subdomain_list.splitlines()

for sub in subdomains:
    sub_domains = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domains)

    except requests.ConnectionError:
        pass

    else:
        print("Valid domain: ",sub_domains)
