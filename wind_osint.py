#WindOSINT
from bs4 import BeautifulSoup
import requests
import sys
import whois
import re
import json

# whois
def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return {"error": str(e)}

# sys
def sysinfo():
    try:
        return sys.version
    except Exception as e:
        return {"error": str(e)}

# re
def re_search(pattern, text):
    try:
        match = re.search(pattern, text)
        return match.group(0) if match else None
    except Exception as e:
        return {"error": str(e)}

# requests
def requests_get(URL):
    try:
        response = requests.get(URL)
        return response
    except Exception as e:
        return {"error": str(e)}

# beautifulSoup
def soup(html_content):
    try:
        return BeautifulSoup(html_content, 'html.parser')
    except Exception as e:
        return {"error": str(e)}

# json
def json_load(json_string):
    try:
        return json.loads(json_string)
    except Exception as e:
        return {"error": str(e)}

if not whois_lookup:
    print("whois_lookup not found")

if not sysinfo:
    print("sysinfo not found")

if not re_search:
    print("re_search not found")

if not requests_get:
    print("requests_get not found")

if not soup:
    print("soup not found")

if not json_load:
    print("json_load not found") 

#Input
domain = input("Domain: ")
url = input("URL: ")
pattern = input("Pattern: ")
text = input("Text: ")

print(whois_lookup(domain))
response = requests_get(url)
if isinstance(response, dict) and "error" in response:
    print(response)
else:
    print(response.text[:500], "...")

print(sysinfo())
print(re_search(pattern, text))
