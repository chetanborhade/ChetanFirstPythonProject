import requests
import json

url = "https://wwww.googleapis.com/urlshortener/v1/url"
payload = {"longUrl": "http://example.com"}
headers = {"content-type": "application/json"}
r = requests.post(url, json=payload, headers=headers)

print(r.headers)