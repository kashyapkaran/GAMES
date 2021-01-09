import requests

payload = {'page':2,'count':25}
r = requests.get('https://httpbin.org/post',params=payload)

print(r.url)
