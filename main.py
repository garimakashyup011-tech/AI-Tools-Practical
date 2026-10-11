
import requests

try:
    response = requests.get("https://example.com", timeout=10)
    response.raise_for_status()
    print("Website accessed successfully")
    print("Status code:", response.status_code)
except requests.RequestException as error:
    print("Request failed:", error)
