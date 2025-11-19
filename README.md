# WindOSINT

WindOSINT is a simple and modular OSINT toolkit built in Python.  
This project allows you to perform domain lookups, HTTP requests, regex searches, JSON parsing, and HTML parsing easily.

## Functions

- `whois_lookup(domain)` : Returns the WHOIS information for a given domain.
- `sysinfo()` : Returns Python and system information.
- `re_search(pattern, text)` : Performs a regex search and returns the first match.
- `requests_get(URL)` : Sends a GET request to the given URL.
- `soup(html_content)` : Parses HTML content and returns a BeautifulSoup object.
- `json_load(json_string)` : Converts a JSON string into a Python dictionary.

## Installation

```bash
git clone https://github.com/ruzgarcyber/WindOSINT
cd WindOSINT
pip install -r requirements.txt  # If any additional packages are needed
```

## Usage Example
from WindOSINT import whois_lookup, requests_get, sysinfo, re_search, soup, json_load

WHOIS lookup
print(whois_lookup("example.com"))

HTTP request
response = requests_get("https://example.com")
print(response.text[:500])  # Show only the first 500 characters

System info
print(sysinfo())

Regex search
pattern = r"\b\w+@\w+\.\w+\b"
text = "Email: example@mail.com"
print(re_search(pattern, text))

## Contributing
Feel free to fork the project and send pull requests.
You can report issues or suggest improvements via the Issues section.

## License
This project is licensed under the MIT License.
