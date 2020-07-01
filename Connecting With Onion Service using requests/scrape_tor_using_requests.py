"""
import requests

def get_tor_session():
    session = requests.session()
    #45.112.57.110:6699
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9150',
                       'https': 'socks5://127.0.0.1:9150'}
    return session

# Make a request through the Tor connection
# IP visible through Tor
session = get_tor_session()
print(session.get("ednf5xiofeunsycu.onion/wiki-onion-urls.html").text)
# Above should print an IP different than your public IP

# Following prints your normal public IP
#print(requests.get("http://httpbin.org/ip").text)
"""

import requests
session = requests.session()
session.proxies = {'http':  'socks5h://localhost:9150',
                   'https': 'socks5h://localhost:9150'}
print(session.get('http://httpbin.org/ip').text) # prints {"origin": "67.205.146.164" }

print(requests.get('http://httpbin.org/ip').text) # prints {"origin": "5.102.254.76" }

print(session.get('http://nzxj65x32vh2fkhk.onion/all').text) # Prints the contents of the page
#http://ednf5xiofeunsycu.onion/wiki-onion-urls.html
