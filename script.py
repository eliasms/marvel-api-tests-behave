from turtle import title
from dotenv import load_dotenv
load_dotenv()
import os
import hashlib
from datetime import datetime
import requests
import json

print(os.environ["PUBLIC_KEY"])

ts = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

print("date and time =", ts)

public_key = os.environ["PUBLIC_KEY"]
private_key = os.environ["PRIVATE_KEY"]
pre_hash = ts+private_key+public_key

hash = hashlib.md5(pre_hash.encode('utf-8')).hexdigest()

print("hash", hash)

params_1 = {
        "apikey": public_key,
        "ts": ts,
        "hash": hash,
        "limit": 5
    }

url = "https://gateway.marvel.com:443/v1/public/stories"

response = requests.get(url, params=params_1)

data = json.loads(response.text)

results = data["data"]["results"]

print(len(results))

for i in range(len(results)):
    title = results[i]["title"]
    print('Title:', i, title)

#print(results[0])

